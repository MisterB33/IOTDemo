from time import sleep
import serial

#ser = serial.Serial('/dev/ttyUSB0', 9600) # Establish the connection on a specific port

def ReadDHT11(ser):
    Samps = 0 #Total Records
    while True:
        Samps +=1
        print("connected!")
        temp = ser.readline() # Read the newest line
        temp = temp.decode('UTF-8').strip()
        data = temp.split(',')
        sleep(.1) # Delay for one tenth of a second
        if Samps == 1:
            Samps = 0
            print('Posting Data..')
            break
    return data
