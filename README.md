# CubeSat_LoRa_Communication

To SetUp: 

1. The File 'server_side.io' is the file for the LoRa Gateway. In this file, there is a lot of commented out lines that you don't need and can be removed. Baseline, the Gateway sets it's communication frequency at 868.0, and in the loop that runs the gateway will continue to check if it recieves data on that frequency. If it does, then it will recieve the packet, print the packet to a console to be watched, then send the packet back out for receiving by another gateway.

