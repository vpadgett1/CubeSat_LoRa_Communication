// Updated on 3/3/2021: Sawaiz, Xiaochun, Ummad and Patrick
//            8/15/2022: Sawaiz and Xiaochun
//                      Fixed an issue of SPI bus lock up
//	      11/16/2022: Tori and Xiaochun
//		       Add serial communication for sending data to remote server
//            12/15/2022: Tori
//                     Changed 'ttyUSB0' serial port to 'ttyUSB1' serial port due to changing out LoRa boards. 
//            1/11/2023: Tori
//                     Updated to send data to CSV called 'thirty_minute_collections.csv' and crossrun transmission every
//                     30 minutes
//
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <wiringSerial.h>

using namespace std;

#include <iostream>
#include <fstream>

#include <time.h>

// Makefile needed
// -lwiringPi

//Global counters
static volatile int counters[] = {0,0,0,0,0,0,0};

// Prototypes
void interrupt0 (void);
void interrupt1 (void);
void interrupt2 (void);
//void interrupt3 (void);
//void interrupt4 (void);
//void interrupt5 (void);
//void interrupt6 (void);

// Argv 1 byte to output.
int main (int argc, char** argv){
  
  if (argc < 2) {
    cout << "You dummy! need to provide an output filename" << endl;
    exit(1);
  }
  
  time_t rawtime;
  struct tm * timeinfo;
  
  ofstream output;
  ofstream datafile;
  
  wiringPiSetup();
  
  //Enable interupts
  wiringPiISR (02, INT_EDGE_RISING,  &interrupt0);  // GPIO27  => CH0 && CH1
  wiringPiISR (01, INT_EDGE_RISING,  &interrupt1);  // GPIO18  => CH0 && CH2
  wiringPiISR (00, INT_EDGE_RISING,  &interrupt2);  // GPIO17  => CH1 && CH2
  
  /* 
  int sfd = serialOpen("/dev/ttyUSB1", 115200);
  if (sfd > 0 ) 
    {
      cout <<  "/dev/ttyUSB1 port is opened successfully! " << endl;
    } else {
    cout << "Can't open /dev/ttyUSB1" << endl;
  }
  */
  
  /*
    while(1) {
    delay(10000);
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    cout << "Current time: " << asctime(timeinfo) << endl;
    //serialPuts(sfd, asctime(timeinfo));
    serialPuts(sfd, " a b c d e f \n \0");
    }
  */

  // FILE *fpt;
  // fpt = fopen("thirty_min_collections.csv", "w+");
  
  char buffer[50];
  char padding[3] = {'*','*', ' '};
  
  while(1){
    delay(60000);
    //delay(6000);
    //std::ofstream datafile("/home/cosmic/mppcInterface/firmware/libraries/slowControl/thirty_min_collections.csv", std::ios::app);
    datafile.open("/home/cosmic/mppcInterface/firmware/libraries/slowControl/thirty_min_collections.csv", std::ofstream::out|std::ofstream::app);
    output.open(argv[1], std::ofstream::out|std::ofstream::app);
    time(&rawtime);
    timeinfo = localtime(&rawtime);
    //printf("%d,%d,%d,%s", counters[2],counters[1],counters[0],asctime(timeinfo));
    sprintf(buffer,"%d, %d, %d, %s", counters[2],counters[1],counters[0],asctime(timeinfo));
    datafile << counters[2] << ", " << counters[1] << ", " << counters[0] << ", " << asctime(timeinfo);
    output << counters[2] << ", " << counters[1] << ", " << counters[0] << ", " << asctime(timeinfo);
    for(int i = 0 ; i < sizeof(counters)/sizeof(counters[0]) ; i ++){
      counters[i] = 0;
    }
    //serialPuts(sfd,buffer);   // sending data to remote server
    output.close();
    printf("%s", buffer);
    datafile.close();
  }

  return 0;
}

void interrupt0 (void){
  counters[0]++ ;
}

void interrupt1 (void){
  counters[1]++ ;
}

void interrupt2 (void){
  counters[2]++ ;
}

/*
void interrupt3 (void){
  counters[3]++ ;
}

void interrupt4 (void){
  counters[4]++ ;
}

void interrupt5 (void){
  counters[5]++ ;
}

void interrupt6 (void){
  counters[6]++ ;
}
*/
