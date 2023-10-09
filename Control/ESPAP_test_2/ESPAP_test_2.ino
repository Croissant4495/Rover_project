#include <WiFi.h>
#include <WiFiUdp.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

// constants
const char *ssid = "ESP_t1";
const char *password = "12345678";
const int localPort = 8888;

// variables
WiFiServer server(localPort);
WiFiUDP udp;

short int mode = 1;

unsigned char packetBuffer[255];
unsigned char sendBuffer[255];

// Function prototypes


void setup() {
  // Setting up serial
  Serial.begin(115200);
  Serial.println();
  Serial.println("Configuring access point...");

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

int temp = 5;
short int num ; 
void loop() {
  // Check for clients
  WiFiClient client = server.available();

  if(client){
    Serial.println("New Client");
    while(client.connected()){
      if (client.available()){
        packetBuffer[0] = client.read();
        packetBuffer[1] = client.read();
        fromBytes(packetBuffer, &num);
        Serial.print("NUM:");
        Serial.println(num);
      }

    }
    Serial.println("Client dissconnected");
  }

}

void fromBytes(unsigned char *byteArray, short int* var1){
  // mode
  *var1 = (short int)(byteArray[1] << 8 | byteArray[0]);
}
