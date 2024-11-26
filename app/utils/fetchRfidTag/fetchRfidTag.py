import ctypes
import binascii

def fetch_rfid_tag():
    # Load the DLL
    try:
        basic_dll = ctypes.CDLL('C:/Windows/SysWOW64/Basic.dll')
    except OSError as e:
        print(f"Error loading DLL: {e}")
        return "00000000000000000000000"
        # exit(1)

    # Define the function name as found in the DLL
    try:
        # Replace 'Inventory_G2' with the actual exported function name
        read_rfid_tag_func = basic_dll.Inventory_G2
    except AttributeError:
        print("The function 'Inventory_G2' was not found in the DLL.")
        return "00000000000000000000000"
        # exit(1)

    # Set the return type of the function if necessary

    read_rfid_tag_func.restype = ctypes.c_int

    # Define parameters
    port = 5
    com_add = ctypes.byref(ctypes.c_ubyte(0xFF))
    baud = ctypes.c_ubyte(4)
    frm_handle = ctypes.byref(ctypes.c_int(port))
    ConAddr = ctypes.byref(ctypes.c_byte(0xFF))
    AdrTID = ctypes.c_byte(0)
    LenTID = ctypes.c_byte(0)
    TIDFlag = ctypes.c_byte(0)
    EPClenandEPC = (ctypes.c_byte * 13)()  # Array to hold EPC data
    Totallen = ctypes.byref(ctypes.c_int(0))  # Total length of EPC
    CardNum = ctypes.byref(ctypes.c_int(0))   # Card number
    PortHandle = ctypes.c_int(port)

    # Open the COM port
    try:
        open_com_port = basic_dll.OpenComPort(port, com_add, baud, frm_handle)
        print(open_com_port)
        if open_com_port != 0:  # Assuming 0 indicates success
            print("Failed to open COM port.")
            return "00000000000000000000000"
            # exit(1)
    except Exception as e:
        print(f"Error opening COM port: {e}")
        # exit(1)

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
    close_com_port=basic_dll.CloseSpecComPort(port)