import serial
ser = serial.Serial('/dev/ttyAMA0',115200)
#if(ser.isOpen()):
#	print("open")

#key = '1' # stop
#key = '2' # fast
key = '3'  # move robot arm

ser.write(serial.to_bytes([int(key, 16)]))

ser.close()
