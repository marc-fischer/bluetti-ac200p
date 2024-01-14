from pymodbus.client import ModbusSerialClient

serial_port = "COM6"
slave_address = 1
baud_rates = [
    1200,
    2400,
    4800,
    9600,
    19200,
    38400,
    57600,
    115200
]

def read_modbus_rtu_registers(starting_address, quantity, baud):
    # Configure the Modbus RTU client
    client = ModbusSerialClient(
        method='rtu',
        port=serial_port,
        baudrate=baud,
        timeout=1
    )

    # Open the serial connection
    if not client.connect():
        print("Failed to connect to Modbus RTU device.")
        return None

    try:
        # Send the Modbus RTU read request
        result = client.read_holding_registers(starting_address, quantity, unit=slave_address)

        # Check if the request was successful
        if not result.isError():
            return result.registers
        else:
            print(f"Error reading from Modbus RTU device: {result}")
            return None
    finally:
        # Close the serial connection
        client.close()

# Example usage
starting_address = 10
quantity = 6


for baudrate in baud_rates:
    data = read_modbus_rtu_registers(starting_address, quantity, baudrate)
    if data is not None:
        print("Data read from Modbus RTU device:", data)
