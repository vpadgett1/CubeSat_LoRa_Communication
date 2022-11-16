import serial
import socket
import os
import time

while True:
    try:
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
        if ser.is_open:
            while True:
                size = ser.inWaiting()
                if size:
                    data = ser.read(size)
                    res = data.decode("utf-8")
                    print(res)
                    with open('from_other_satellites.csv', 'a') as file:
                    file.write(str(res))
                    file.write("\n")
                    print("line written")
                else:
                    print("Data not reading")
                time.sleep(1)
        else:
            ser.close()
            print("ser is no open or data complete")
    except serial.SerialException:
        print("USB0 Not Open")
        time.sleep(1)
