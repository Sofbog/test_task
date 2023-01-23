
import serial

# Set up the serial connection to the Arduino
ser = serial.Serial('COM3', 9600)

# Set the input range and NPLC
ser.write(b'CONF:VOLT:DC 0,3.3') # Input range 0..3.3V

# Read the voltage measurement for different NPLC
for nplc in [1, 5, 10]:
    ser.write(f'VOLT:DC:NPLC {nplc}'.encode())
    ser.write(b'READ?')
    voltage = float(ser.readline())
    print(f"Voltage at NPLC {nplc}: {voltage}")

# Close the serial connection
ser.close()
