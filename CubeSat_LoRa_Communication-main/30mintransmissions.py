import serial
import socket
import os
import time
import schedule
  
def send_data():
    with open('30_Updates.csv', 'r+') as file:
        #Get Data from Dr. He's OutPut Collection (In His Script, save to CSV):
        lines = file.readlines()
        for line in lines:
            ser.write(line)
            time.sleep(0.5)
        #clear file for next round of 30 minute transmission    
        file.truncate(0)
            
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)       
  
schedule.every(30).minutes.do(send_data)
  
while True:
    schedule.run_pending()
    time.sleep(1500)