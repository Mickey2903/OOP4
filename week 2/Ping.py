import serial
import time
ser = serial.Serial('COM4',9600,timeout=1)
 
while 1:
 try:
  print(ser.read(4).decode("utf-8") + "\n")
  time.sleep(1)
 except ser._timeout:
  print('Data could not be read')
  time.sleep(1)