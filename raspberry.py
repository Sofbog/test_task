import serial

# Set up the serial connection to the Raspberry Pi
ser = serial.Serial('COM3', 9600)

# Set the input range and NPLC
ser.write(b'CONF:VOLT:DC 0,3.3') # Input range 0..3.3V
ser.write(b'VOLT:DC:NPLC 1') # NPLC: 1

# Read the voltage measurement
ser.write(b'READ?')
voltage = float(ser.readline())
print("Voltage: ", voltage)

# Change the NPLC
ser.write(b'VOLT:DC:NPLC 5') # NPLC: 5

# Read the voltage measurement
ser.write(b'READ?')
voltage = float(ser.readline())
print("Voltage: ", voltage)

# Change the NPLC
ser.write(b'VOLT:DC:NPLC 10') # NPLC: 10

# Read the voltage measurement
ser.write(b'READ?')
voltage = float(ser.readline())
print("Voltage: ", voltage)

# Close the serial connection
ser.close()



