# CubeSat_LoRa_Communication

To SetUp: 

1. The File 'server_side.io' is the file for the LoRa Gateway. In this file, there is a lot of commented out lines that you don't need and can be removed. Baseline, the Gateway sets it's communication frequency at 868.0, and in the loop that runs the gateway will continue to check if it recieves data on that frequency. If it does, then it will recieve the packet, print the packet to a console to be watched, then send the packet back out for receiving by another gateway.

2. The file 'client_side.io' is the current script being run on the LoRa boards individually. This script will send any data it recieves through Serial communication out to the gateway. As well, in the loop, the LoRa board will look for any data being communicated to it on frequency 868.0 and will then use a serial connection to send this data back to the Pi. 

3. The Raspberry Pi will need to be running the 'pireceive.py' script. This script is out of date and has been edited but the idea is similar to what I have here originally. The file will constantly run on the Pi, using the while True loop, and will look for any data being serially communicated. It will then receieve the data, and will write it to a CSV file that will store all of the data. 

4. The 'pisend.py' file is used if you need to communicate data from a Raspberry Pi serially for transmission. If you do not, then this script may not apply. It will also need to run on that pi forever to make sure the data is being sent. 

5. All other files included are support files for the communication system. They should not be needed in the overall communication. 

If you have any question, please reach out to me and I'll be happy to answer. 
