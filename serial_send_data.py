import serial
import socket
import os
import time
import schedule
import datetime
import csv
from serial.serialutil import SerialException

# def send_data():
#     with open('/home/cosmic/mppcInterface/firmware/libraries/slowControl/thirty_min_collections.csv', 'r+') as file:
#         lines = file.readlines()
#         for line in lines:
#             print("Og line: " + line)
#             byte_str =bytes(line, 'utf-8')
#             print("Byte String: " + str(byte_str))
#             ser.write(byte_str)
#             time.sleep(4)

#         print("wrote 30 lines of data to serial port")

def get_last_timestamp(last_timestamp, serial_port):
    # Read CSV file, filter data based on last sent timestamp,
    # add device name to each row, and convert to JSON
    with open("/home/cosmic/mppcInterface/firmware/libraries/slowControl/thirty_min_collections.csv",'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        data = [
            {
                "Chan_0_1": int(row["Chan_0_1"]),
                "Chan_0_2": int(row["Chan_0_2"]),
                "Chan_1_2": int(row["Chan_1_2"]),
                "timestamp": datetime.datetime.strptime(str(row["timestamp"]).strip(), "%a %b  %d %H:%M:%S %Y").strftime("%a %b  %d %H:%M:%S %Y"),
            }
            for row in csv_reader
            if datetime.datetime.strptime(str(row["timestamp"]).strip(), "%a %b  %d %H:%M:%S %Y") > datetime.datetime.strptime(last_timestamp, '%a %b  %d %H:%M:%S %Y')
        ]
    if len(data) == 0:
        return last_timestamp
    else:
        for row in data:
            string_send = f"{row['Chan_0_1']},{row['Chan_0_2']},{row['Chan_1_2']},{row['timestamp']}"
            byte_str = bytes(string_send, 'utf-8')
            try:
                serial_port.write(byte_str)
            except SerialException as e:
                print("An Exeception occured with serial transmission", e)
            with open("/home/cosmic/mppcInterface/firmware/libraries/slowControl/last_sent_timestamp.txt",'w') as file:
                file.write(f"{row['timestamp']}")
            time.sleep(10)
        
    # Return the last timestamp from the filtered CSV data
    last_row = data[-1] if data else None
    last_timestamp = last_row["timestamp"] if last_row else last_timestamp
    return last_timestamp
# Define function to schedule sending task every 30 minutes at regular times of the day
def schedule_get_last_timestamp(ser_port):
    # Initialize last sent timestamp to the earliest possible timestamp
    #last_timestamp = datetime.datetime.combine(datetime.date.today(),datetime.datetime.min.time()).strftime("%a %b  %d %H:%M:%S %Y")
    last_timestamp = ""
    with open("/home/cosmic/mppcInterface/firmware/libraries/slowControl/last_sent_timestamp.txt",'r') as csv_file:
        last_timestamp = csv_file.read()
        # if datetime.datetime.strptime(str(last_line["timestamp"]).strip(), "%a %b  %d %H:%M:%S %Y") > datetime.datetime.strptime(last_timestamp, '%a %b  %d %H:%M:%S %Y')
        
    print(last_timestamp)
    print(' in scheduling')
    while True:
        now = datetime.datetime.now()
        if now.minute == 0 or now.minute == 30:
            # Define the times of the day when the CSV da                                                               ta should be sent
            # send_times = [datetime.time(hour=h, minute=0) for h in range(0, 24)] + \
            #              [datetime.time(hour=h, minute=30) for h in range(0, 24)] + \
            #              [datetime.time(hour=h, minute=10) for h in range(0, 24)]
            # print('here')
            # print(send_times)
            # print(now.time())
            # Check if the current time is one of the send times
            print('inner loop')
            # Send CSV data and update last sent timestamp
            while True:
                last_timestamp = get_last_timestamp(last_timestamp, ser_port)
                break
                

        time.sleep(10)

# Run scheduling task indefinitely
def main():
    while True:
        #try:
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=.1)
        print("success")
        # except serial.serialutil.SerialException:
        #     print("UnSuccessful Connection to Serial Port")
        print('in main')
        schedule_get_last_timestamp(ser)

if __name__ == "__main__":
    main()