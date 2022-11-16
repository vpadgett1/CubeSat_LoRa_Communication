import serial
import socket
import os
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
time.sleep(5)

# hostname = socket.gethostname()  # IP address of host device
# host = socket.gethostbyname(hostname)
# port = 65432
# HEADERSIZE = 10
# WiFi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # attaching to IP and socket stream
# WiFi.bind((host, port))  # bind to ip
# print(f'socket bound to {host}:{port}')
# WiFi.listen(5)

#while True:
if os.path.exists('sampledata.csv'):
#print("path exists")
    with open('sampledata.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = bytes(line, 'utf-8')
        #print(arr)
            ser.write(arr)
        #print(ser.readline())
        #print("written")
            time.sleep(1)
            recv_from_cube = ser.readline()
            string_data = str(recv_from_cube)
            print(string_data)
        #if(string_data == "b'got reply: received\r\n'"):
            #print("recieved")
        #else:
            with open('from_other_satellites.csv', 'a') as file:
                file.write(str(recv_from_cube))
                file.write("\n")
                print("line written")
            time.sleep(1)
            #ser.flush()
