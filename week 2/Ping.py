import serial
import time
ser = serial.Serial('COM6',9600,timeout=1)
 
while 1:
 try:
  print(ser.readline().decode("utf-8"))
  time.sleep(1)
 except ser.SerialTimeoutException:
  print('Data could not be read')
  time.sleep(1)