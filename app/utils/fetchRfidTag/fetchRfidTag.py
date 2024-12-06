import ctypes
import binascii

def open_com_port():
    # Load the DLL
    global basic_dll
    try:
        # basic_dll = ctypes.CDLL('C:/Windows/SysWOW64/Basic.dll')
        basic_dll = ctypes.CDLL('D:/Starlabs/rfid-dll/Basic.dll')
    except OSError as e:
        print(f"Error loading DLL: {e}")
        return "00000000000000000000000"
        # exit(1)

    # Define parameters
    port = 5
    com_add = ctypes.byref(ctypes.c_ubyte(0xFF))
    baud = ctypes.c_ubyte(4)
    frm_handle = ctypes.byref(ctypes.c_int(port))

    # Open the COM port
    try:
        open_com_port = basic_dll.OpenComPort(port, com_add, baud, frm_handle)
        if open_com_port:  # Assuming 0 indicates success
            print("Failed to open COM port.")
            return "00000000000000000000000"
            # exit(1)
    except Exception as e:
        print(f"Error opening COM port: {e}")
        # exit(1)

def fetch_rfid_tag():  
    # Define the function name as found in the DLL
    try:
        # Replace 'Inventory_G2' with the actual exported function name
        read_rfid_tag_func = basic_dll.Inventory_G2
    except AttributeError:
        print("The function 'Inventory_G2' was not found in the DLL.")
        return "00000000000000000000000"
        # exit(1)

    # Set the return type of the function if necessary
    # Define parameters
    port=5
    com_add = ctypes.byref(ctypes.c_ubyte(0xFF))
    AdrTID = ctypes.c_byte(0)
    LenTID = ctypes.c_byte(0)
    TIDFlag = ctypes.c_byte(0)
    EPClenandEPC = (ctypes.c_byte * 13)()  # Array to hold EPC data
    Totallen = ctypes.byref(ctypes.c_int(0))  # Total length of EPC
    CardNum = ctypes.byref(ctypes.c_int(0))   # Card number
    PortHandle = ctypes.c_int(port)

    read_rfid_tag_func.restype = ctypes.c_int

    while True:
        # Call the read RFID tag function
        try:
            read_rfid_tag = read_rfid_tag_func(com_add, AdrTID, LenTID, TIDFlag, EPClenandEPC, Totallen, CardNum, PortHandle)
            print(f"Read RFID Tag Result: {read_rfid_tag}")
        except Exception as e:
            print(f"Error reading RFID tag: {e}")
            return "00000000000000000000000"
            # exit(1)

        # Convert the EPC byte array to a hex string
        byte_array = EPClenandEPC
        hex_string = binascii.hexlify(byte_array).decode('utf-8')
        print("EPC Hex String:", hex_string.upper()[2:])
        return(hex_string.upper()[2:])

def close_com_port():
    global basic_dll
    if basic_dll:
        try:
            port=5
            print("Closing Comport")
            close_com=basic_dll.CloseSpecComPort(port)
            print(f"COM port closed: {close_com}")
            del basic_dll
            basic_dll = None

        except Exception as e:
                print(f"Error closing COM port: {e}")



'''
1. Create a function to open the com-port. It will open once when the Internal RFID form gets clicked
2. While clicking on the fetch button the data will be fetched from the Inventory function
Note: COM-Port will be open single time and the Inventory function data will come multiple times
'''