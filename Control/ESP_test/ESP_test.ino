#include <WiFi.h>
#include <WiFiUdp.h>


// WIFI VARIABLES
// WiFi network name and password:
const char * networkName = "Galaxy A34";
const char * networkPswd = "1234567@";

//IP address to send UDP data to:
// either use the ip address of the server or 
// a network broadcast address
const char * udpAddress = "192.168.1.9";
const int udpPort = 8888;

//Are we currently connected?
boolean connected = false;

//The udp library class
WiFiUDP udp;

// Recieved Data
short int mode = 1;
short int motion;

// Sent data
short int distance = 350;
int encoder = 12345678;

int counter = 0;
unsigned char packetBuffer[255]; //buffer to hold incoming packet
unsigned char sendArray[255];

void toBytes(unsigned char *byteArray, short int mode, short int distance, int encoder) {
    // mode
    byteArray[0] = (unsigned char)(mode & 0xFF); 
    //distance
    byteArray[1] = (unsigned char)(distance & 0xFF);
    distance >>= 8;          
    byteArray[2] = (unsigned char)(distance & 0xFF);
    // encoder
    byteArray[3] = (unsigned char)(encoder & 0xFF);
    encoder >>= 8;           
    byteArray[4] = (unsigned char)(encoder & 0xFF);
    encoder >>= 8;           
    byteArray[5] = (unsigned char)(encoder & 0xFF);
    encoder >>= 8;           
    byteArray[6] = (unsigned char)(encoder & 0xFF);
}

void fromBytes(unsigned char *byteArray, short int* mode, short int* motion){
  // mode
  *mode = (short int)(byteArray[1] << 8 | byteArray[0]);
}


void setup(){
  // Initilize hardware serial:
  Serial.begin(9600);
  //Connect to the WiFi network
  connectToWiFi(networkName, networkPswd);
}
int sent = 0;
void loop(){
  //only send data when connected
  if(connected){
    //Send a packet
    send_packet();
  }
  received_packet();
}

void send_packet(){
    toBytes(sendArray, mode, distance, encoder);
    udp.beginPacket(udpAddress,udpPort);
    udp.write(sendArray, 7);
    udp.endPacket();
}

void received_packet(){
  int size = 0;
  size = udp.parsePacket();
  if (size){
    Serial.println(size);
    udp.read(packetBuffer, 255);
    fromBytes(packetBuffer, &mode, &motion);
    Serial.println(mode);
  }else{
    //Wait for 1 second
    delay(1000);
  }
}

void connectToWiFi(const char * ssid, const char * pwd){
  Serial.println("Connecting to WiFi network: " + String(ssid));

  // delete old config
  WiFi.disconnect(true);
  //register event handler
  WiFi.onEvent(WiFiEvent);
  
  //Initiate connection                                                                            
  WiFi.begin(ssid, pwd);
  Serial.println("Waiting for WIFI connection...");
}

//wifi event handler
void WiFiEvent(WiFiEvent_t event){
    switch(event) {
      case ARDUINO_EVENT_WIFI_STA_GOT_IP:
          //When connected set 
          Serial.print("WiFi connected! IP address: ");
          Serial.println(WiFi.localIP());  
          //initializes the UDP state
          //This initializes the transfer buffer
          udp.begin(WiFi.localIP(),udpPort);
          connected = true;
          break;
      case ARDUINO_EVENT_WIFI_STA_DISCONNECTED:
          Serial.println("WiFi lost connection");
          connected = false;
          break;
      default: break;
    }
}
