import serial
import socket
import os
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=7000, timeout=.1)

hostname = socket.gethostname()  # IP address of host device
host = socket.gethostbyname(hostname)
port = 65432
HEADERSIZE = 10
WiFi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # attaching to IP and socket stream
WiFi.bind((host, port))  # bind to ip
print(f'socket bound to {host}:{port}')
WiFi.listen(5)



if os.path.exists('/home/pi/Downloads/sampledata.csv'):
    with open('/home/pi/Downloads/sampledata.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            arr = bytes(line, 'utf-8')
            ser.write(arr)
            ser.flush()
