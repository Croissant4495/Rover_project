#include "WiFi.h"

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

void toBytes(unsigned char *byteArray, short int var1) {
    // mode
    byteArray[0] = (unsigned char)(var1 & 0xFF); 
}

void fromBytes(unsigned char *byteArray, short int* var1, short int* var2, short int* var3, short int* var4){
  // mode
  *var1 = (short int)(byteArray[1] << 8 | byteArray[0]);
  // speed1
  *var2 = (short int)(byteArray[3] << 8 | byteArray[2]);
  // speed2
  *var3 = (short int)(byteArray[5] << 8 | byteArray[4]);
  // speed2
  *var4 = (short int)(byteArray[7] << 8 | byteArray[6]);
}

void send_packet(){
    // toBytes(sendArray, mode);
}

void recv_bytes(WiFiClient* client_ptr, short int* var1, short int* var2, short int* var3, short int* var4){
  for (int i = 0; i<= rcv_message_length; i++){
    packetBuffer[i] = client_ptr->read();
    }
  fromBytes(packetBuffer, var1, var2, var3, var4);
  Serial.print("Mode: ");
  Serial.println(*var1);
  Serial.print("Speed1: ");
  Serial.println(*var2);
  Serial.print("Speed2: ");
  Serial.println(*var3);
  Serial.print("Gripper_mode: ");
  Serial.println(*var4);
}