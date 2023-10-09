#include <WiFi.h>
#include <WiFiUdp.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

// WIFI VARIABLES
// Set these to your desired credentials.
const char *ssid = "ESP_t1";
const char *password = "12345678";
const unsigned int localPort = 8888;

WiFiServer server(localPort);

//The udp library class
WiFiUDP udp;

// Recieved Data
short int mode = 1;

unsigned char packetBuffer[255]; //buffer to hold incoming packet
unsigned char sendArray[255];

void setup(){
  // Initilize hardware serial:
  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");

  // You can remove the password parameter if you want the AP to be open.
  // a valid password must have more than 7 characters
  if (!WiFi.softAP(ssid, password)) {
    log_e("Soft AP creation failed.");
    while(1);
  }
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  Serial.println("Server started");
  
}

void loop(){
  // rcv_packet();
  WiFiClient client = server.available();   // listen for incoming clients

  if (client){
    Serial.println("New Client.");
    while(client.connected()){
      if (client.available()){
        String recieved = client.readStringUntil('\r');
        Serial.println(recieved);
      }
    }
  }

}

void start_server(){
  Serial.println();
  Serial.println("Configuring access point...");

  // You can remove the password parameter if you want the AP to be open.
  // a valid password must have more than 7 characters
  if (!WiFi.softAP(ssid, password)) {
    log_e("Soft AP creation failed.");
    while(1);
  }
  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);
  server.begin();

  Serial.println("Server started");
}

// void send_packet(){
//     toBytes(sendArray, mode, distance, encoder);
//     udp.beginPacket(udpAddress,udpPort);
//     udp.write(sendArray, 7);
//     udp.endPacket();
// }

void rcv_packet(){
  int size = 0;
  size = udp.parsePacket();
  if (size){
    Serial.println(size);
    udp.read(packetBuffer, 255);
    fromBytes(packetBuffer, &mode);
    Serial.println(mode);
  }else{
    //Wait for 1 second
    delay(1000);
  }
}

// void connectToWiFi(const char * ssid, const char * pwd){
//   Serial.println("Connecting to WiFi network: " + String(ssid));

//   // delete old config
//   WiFi.disconnect(true);
//   //register event handler
//   WiFi.onEvent(WiFiEvent);
  
//   //Initiate connection                                                                            
//   WiFi.begin(ssid, pwd);
//   Serial.println("Waiting for WIFI connection...");
// }

// //wifi event handler
// void WiFiEvent(WiFiEvent_t event){
//     switch(event) {
//       case ARDUINO_EVENT_WIFI_STA_GOT_IP:
//           //When connected set 
//           Serial.print("WiFi connected! IP address: ");
//           Serial.println(WiFi.localIP());  
//           //initializes the UDP state
//           //This initializes the transfer buffer
//           udp.begin(WiFi.localIP(),udpPort);
//           connected = true;
//           break;
//       case ARDUINO_EVENT_WIFI_STA_DISCONNECTED:
//           Serial.println("WiFi lost connection");
//           connected = false;
//           break;
//       default: break;
//     }
// }

// void toBytes(unsigned char *byteArray, short int mode, short int distance, int encoder) {
//     // mode
//     byteArray[0] = (unsigned char)(mode & 0xFF); 
//     //distance
//     byteArray[1] = (unsigned char)(distance & 0xFF);
//     distance >>= 8;          
//     byteArray[2] = (unsigned char)(distance & 0xFF);
//     // encoder
//     byteArray[3] = (unsigned char)(encoder & 0xFF);
//     encoder >>= 8;           
//     byteArray[4] = (unsigned char)(encoder & 0xFF);
//     encoder >>= 8;           
//     byteArray[5] = (unsigned char)(encoder & 0xFF);
//     encoder >>= 8;           
//     byteArray[6] = (unsigned char)(encoder & 0xFF);
// }

void fromBytes(unsigned char *byteArray, short int* mode){
  // mode
  *mode = (short int)(byteArray[1] << 8 | byteArray[0]);
}

