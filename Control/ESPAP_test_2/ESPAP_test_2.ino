#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

#define rcv_message_length 6

// constants
const char *ssid = "ESP_t1";
const char *password = "12345678";
const int localPort = 8888;

// variables
WiFiServer server(localPort);

unsigned char packetBuffer[255];
unsigned char sendBuffer[255];

// Function prototypes


void setup() {
  // Setting up serial
  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");
  start_server();
}

short int mode = 7;
short int speed1 = 150;
short int speed2 = 150; 

void loop() {
  // Check for clients
  WiFiClient client = server.available();

  if(client){
    Serial.println("New Client");
    while(client.connected()){
      if (client.available() >= 6){
        recv_bytes(&client);
      }
    }
    Serial.println("Client dissconnected");
  }
  // Serial.println("Rest of code");
}

void start_server(){
  // Setting up access point
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

void recv_bytes(WiFiClient* client_ptr){
  for (int i = 0; i<= rcv_message_length; i++){
    packetBuffer[i] = client_ptr->read();
    }
  fromBytes(packetBuffer, &mode, &speed1, &speed2);
  Serial.print("Mode: ");
  Serial.println(mode);
  Serial.print("Speed1: ");
  Serial.println(speed1);
  Serial.print("Speed2: ");
  Serial.println(speed2);
}

void fromBytes(unsigned char *byteArray, short int* var1, short int* var2, short int* var3){
  // mode
  *var1 = (short int)(byteArray[1] << 8 | byteArray[0]);
  // speed1
  *var2 = (short int)(byteArray[3] << 8 | byteArray[2]);
  // speed2
  *var3 = (short int)(byteArray[5] << 8 | byteArray[4]);
}
