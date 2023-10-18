#ifndef _WIFI_H_
#define _WIFI_H_
//_________Libraries_________
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

// _________WIFI_VARIABLES_________
#define rcv_message_length 8
extern const char *ssid;
extern const char *password;
extern const int localPort;

extern WiFiServer server;

extern unsigned char packetBuffer[255]; //buffer to hold incoming packet
extern unsigned char sendArray[255];

//_________WIFI_functions_________
void toBytes(unsigned char *byteArray, short int var1);
void fromBytes(unsigned char *byteArray, short int* var1, short int* var2, short int* var3, short int* var4);
void start_server();

void send_packet();
void recv_bytes(WiFiClient* client_ptr, short int* var1, short int* var2, short int* var3, short int* var4);
#endif