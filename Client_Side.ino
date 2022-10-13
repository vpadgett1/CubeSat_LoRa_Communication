#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;
float frequency = 868.0;
const int BUFFER_SIZE = 100;
uint8_t buf[BUFFER_SIZE];

void setup() 
{
  Serial.begin(115200);
  //while (!Serial) ; // Wait for serial port to be available
  Serial.println("Start LoRa Client");
  if (!rf95.init())
    Serial.println("init failed");
  // Setup ISM frequency
  rf95.setFrequency(frequency);
  // Setup Power,dBm
  rf95.setTxPower(13);

  // Setup Spreading Factor (6 ~ 12)
  rf95.setSpreadingFactor(7);
  
  // Setup BandWidth, option: 7800,10400,15600,20800,31200,41700,62500,125000,250000,500000
  //Lower BandWidth for longer distance.
  rf95.setSignalBandwidth(125000);
  
  // Setup Coding Rate:5(4/5),6(4/6),7(4/7),8(4/8) 
  rf95.setCodingRate4(5);
}

void loop()
{
  //Serial.println("Sending to LoRa Server");
  // Send a message to LoRa Server
  //uint8_t data[] = "Hello, this is device 1";
  //rf95.send(data, sizeof(data));
  while(Serial.available()){ 
    Serial.readBytesUntil('\n',buf,BUFFER_SIZE);
    rf95.send(buf, sizeof(buf)); //Send buf
    rf95.waitPacketSent();
    // Now wait for a reply
    uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(buf);

    if (rf95.waitAvailableTimeout(3000))
    { 
    // Should be a reply message for us now   
      if (rf95.recv(buf, &len))
      {
        Serial.println("got reply: ");
        uint8_t reply = buf;
        //if(((char*)reply) == "Recieved"){
          //Serial.write((char*)reply);
        //}
        //else{
        Serial.println((char*)buf);
        //}
      //Serial.print("RSSI: ");
      //Serial.println(rf95.lastRssi(), DEC);    
      }
      else
      {
        Serial.println("recv failed");
      }
    }
    else
    {
      Serial.println("No reply, is LoRa server running?");
    }
  }
}
