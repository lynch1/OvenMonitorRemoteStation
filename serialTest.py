import serial
import  time
import io

sp = serial.Serial(port = "/dev/ttyUSB0", baudrate = 57600, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = 1)

#sp.open()

#sp.write("\r")
#time.sleep(1)

qmsg  = bytearray("?:3010:00::c2\r", "ascii")
sp.write(qmsg)
line = sp.readline()
print(line)
