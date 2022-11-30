import serial
import socket
import os
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
#time.sleep(2)
previous = ''
while True:
    while ser.in_waiting:
        recv_from_cube = ser.readline()
        string_data = str(recv_from_cube)
        with open('final_receving.csv', 'a') as file:
            #if b'recv failed' in recv_from_cube:
                #continue
            string_clean= string_data.split('e\\', 1)
            string_cleaner=string_data.split('2\\xcc', 1)
            #print(string_clean[0])
            if previous==string_clean[0]:
                continue
            clean = string_clean[0].split('b\'',1)
            cleaner = string_cleaner[0].split('b\'',1)
            print(clean)
            #file.write(clean[1])
            #file.write("\n")
            file.write(cleaner[1])
            file.write("\n")
            previous = string_clean[0]
            #print("line written")
        ser.flush()
