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
        print(string_data)
        with open('data_Jan_2023.csv', 'a') as file:
            #if b'recv failed' in recv_from_cube:
                #continue
            #string_clean= string_data.split('e\\', 1)
            #string_cleaner=string_data.split('2\\xcc', 1)
            #print(string_clean[0])
            #string_clean = recv_from_cube.decode('ascii')
            #print(string_clean)
            string_clean = string_data.split('b\'', 1)[1]
            if string_clean.startswith("v"):
                continue
            if string_clean.startswith("\\x"):
                continue
            if string_clean.startswith("H"):
                continue
            if string_clean.startswith("X"):
                continue
            #if "d\r" in string_clean:
                #string_clean.replace("d\r", "")
            if "d\\r" in string_clean:
                string_clean.replace("d\\r", "")
            string_clean = string_clean.split('\\n',1)[0]
            #print(string_clean)
            if previous==string_clean or string_clean.isspace():
                continue
            print("after cleaning:" + string_clean)
            file.write(string_clean)
            file.write('\n')
            previous=string_clean
            #print(string_clean)
        ser.flush()
