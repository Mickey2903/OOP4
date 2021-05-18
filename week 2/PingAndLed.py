import keyboard
import serial
import time
ser = serial.Serial('COM3',9600,timeout=1)

while 1:
    if keyboard.is_pressed(79):
        ser.write('1'.encode('utf-8'))
    elif keyboard.is_pressed(82):
        ser.write('0'.encode('utf-8'))
    try:
        print(ser.readline().decode("utf-8"))
    except ser.SerialTimeoutException:
        print('Data could not be read')
