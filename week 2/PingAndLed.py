import keyboard
import serial
import threading
import logging
import time

ser = serial.Serial('COM4',9600,timeout=1)

#thread function
def thread_Serial():

    #thread loop
    while 1:

        #delay of 1 second
        #data comes in every 1 second
        time.sleep(1)

        #reading and logging data 
        try:
            logging.info(ser.read(4).decode("utf-8") + '\n')
        except ser.SerialTimeoutException:
            logging.info('Data could not be read')



    
if __name__ == "__main__":

    #Logging initialisation
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    #Thread initialisation & start
    SerialThread = threading.Thread(target=thread_Serial, args=())
    SerialThread.start()

    #main loop
    while 1:
        time.sleep(1)

        if keyboard.is_pressed(79):         #press numbpad 1 to activate LED on arduino
            ser.write('1'.encode('utf-8'))      #sends command to arduino to activate LED
            logging.info("Led --> ON") 
        elif keyboard.is_pressed(82):       #press numbpad 0 to deactivate led on arduino
            ser.write('0'.encode('utf-8'))      #sends command to arduino to deactivate LED
            logging.info("Led --> OFF")
            