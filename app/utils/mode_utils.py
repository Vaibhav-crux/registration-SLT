import ctypes
import platform
import winreg
import os
from PyQt5.QtCore import Qt

# Path to the mode configuration file
MODE_FILE_PATH = 'app/data/mode.txt'

def is_dark_mode():
    """Detect if the system is in dark mode, first checking the file, then the system setting."""
    # First, check if the mode.txt file exists and is not empty
    if os.path.exists(MODE_FILE_PATH):
        try:
            with open(MODE_FILE_PATH, 'r') as file:
                mode_value = file.read().strip()

                # Check if the value is valid (0 or 1)
                if mode_value == '0':
                    return True  # Dark mode
                elif mode_value == '1':
                    return False  # Light mode
        except Exception as e:
            print(f"Error reading mode file: {e}")

    # If the file is not found or invalid, fallback to system mode detection
    if platform.system() == 'Windows':
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            return value == 0  # 0 means dark mode, 1 means light mode
        except Exception as e:
            print(f"Error checking dark mode in system settings: {e}")

    # If any error occurs or system not supported, return dark mode by default
    return True  # Default to dark mode if detection fails


def apply_mode_styles(window):
    """
    Apply the correct mode (dark or light) to the given window without changing the window title.
    :param window: The PyQt window to apply the style to.
    """
    if is_dark_mode():
        window.setStyleSheet("background-color: #2e2e2e; color: white;")  # Dark mode
        set_dark_mode_title_bar(window)
    else:
        window.setStyleSheet("background-color: #ffffff; color: black;")  # Light mode
        set_light_mode_title_bar(window)


def apply_window_flags(window):
    """
    Apply window flags to remove the Help button (?) and show only the close button.
    :param window: The PyQt window to apply the flags to.
    """
    window.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)


def set_dark_mode_title_bar(window):
    """Use Windows API to set the title bar color to dark mode."""
    hwnd = get_window_handle(window)
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20  # This value may change with Windows versions

    def set_window_attribute(hwnd, attribute, value):
        value = ctypes.c_int(value)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, attribute, ctypes.byref(value), ctypes.sizeof(value))

    set_window_attribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, 1)


def set_light_mode_title_bar(window):
    """Use Windows API to set the title bar color to light mode."""
    hwnd = get_window_handle(window)
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20  # This value may change with Windows versions

    def set_window_attribute(hwnd, attribute, value):
        value = ctypes.c_int(value)
        ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, attribute, ctypes.byref(value), ctypes.sizeof(value))

    set_window_attribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, 0)


def get_window_handle(window):
    """Get the window handle (HWND) for the given PyQt window."""
    hwnd = window.winId()
    if isinstance(hwnd, int):  # In some PyQt versions, winId returns an int
        return hwnd
    else:
        return int(hwnd)  # Cast SIP object to int
