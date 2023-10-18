//_________Libraries_________
#include "WiFi.h"
#include "motion.h"

// _________WIFI_VARIABLES_________
const char *ssid = "ESP_t1";
const char *password = "12345678";
const int localPort = 8888;

WiFiServer server(localPort);


unsigned char packetBuffer[255]; //buffer to hold incoming packet
unsigned char sendArray[255];


//_________MOTION_VARIABLES_________
volatile unsigned int counter1 = 0;
int rpm1 = 0;
volatile unsigned int counter2 = 0;
int rpm2 = 0;
volatile unsigned long debounce = 0;

long duration;
short int distance;

int time_old;
int time_new;
float dt;

short int mode = 7;
short int gripper_mode = 0;

// Motor values
float factor = 1;
short int speed1 = 100;
short int speed2 = 100;

// Servo my_servo;

void setup(){
  // Set up pinModes and interrupt
  setup_pins();
  // Begin serial
  Serial.begin(115200);
  Serial.print("Started program");
  time_new = millis();
  //Start server
  start_server();
}

void loop(){
  update_time();
  WiFiClient client = server.available();
  if(client){
    Serial.println("New Client");
    while(client.connected()){
      // main loop
      if (client.available()>= 8){
        recv_bytes(&client, &mode, &speed1, &speed2, &gripper_mode);
        client.flush();
      }
      motion_call();
    }
    Serial.println("Client dissconnected");
  }else{
    stop();
  }
}

