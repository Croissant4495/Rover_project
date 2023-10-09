#include <WiFi.h>
#include <WiFiUdp.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

// Motor A (left) connections
#define enA 14
#define in1 33
#define in2 25
// Motor B (right) connections
#define enB 13
#define in3 26
#define in4 27
// Encoder pins
#define encoder1 34
#define encoder2 35

// WIFI VARIABLES
// WiFi network name and password:
const char *ssid = "ESP_T1";
const char *password = "1234567";

//IP address to send UDP data to:
// either use the ip address of the server or 
// a network broadcast address
const char *udpAddress = "192.168.84.158";
const int udpPort = 8888;

WiFiServer server(80);

//Are we currently connected?
boolean connected = false;

//The udp library class
WiFiUDP udp;

// Recieved Data
short int mode = 7;
short int motion;

unsigned char packetBuffer[255]; //buffer to hold incoming packet
unsigned char sendArray[255];


// MOTION VARIABLES
//Variables
volatile unsigned int counter1 = 0;
int rpm1 = 0;
volatile unsigned int counter2 = 0;
int rpm2 = 0;
static volatile unsigned long debounce = 0;

int desired_speed = 200;

int time_old;
int time_new;
float dt;

// motor values
float factor = 1;
short int speed1 = 100;
short int speed2 = 100;

// input reader
float in_num = 0;

// WIFI functions
void toBytes(unsigned char *byteArray, short int mode);
void fromBytes(unsigned char *byteArray, short int* mode, short int* speed1, short int* speed2);

void connectToWiFi(const char * ssid, const char * pwd);
void WiFiEvent(WiFiEvent_t event);

void send_packet();
void received_packet();


// Move functions
void forward();
void stop();
void get_dist();

void update_time();
void get_rpm();

void recv_serial();

// Interrupt functions
void IRAM_ATTR countPulse1() {
  counter1++;
}

void IRAM_ATTR countPulse2() {
  if(  digitalRead (encoder2) && (micros()-debounce > 500) && digitalRead (encoder2) ) { 
        debounce = micros();
        counter2 ++;
      }
        else ; 
}

void setup(){
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  // //set encoder pins
  // pinMode(encoder1, INPUT_PULLUP);
  // pinMode(encoder2, INPUT_PULLUP);
  // attachInterrupt(encoder1, countPulse1, RISING);
  // attachInterrupt(encoder2, countPulse2, RISING);

  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  time_new = millis();

  Serial.begin(9600);
  //Connect to the WiFi network
  connectToWiFi(networkName, networkPswd);
}

void loop(){
  update_time();
  // noInterrupts();
  // get_rpm();
  // interrupts();
  if(connected){
    send_packet();
  }
  received_packet();

  motion_call();
}

// WIFI
void toBytes(unsigned char *byteArray, short int mode) {
    // mode
    byteArray[0] = (unsigned char)(mode & 0xFF); 
}

void fromBytes(unsigned char *byteArray, short int* mode, short int* speed1, short int* speed2){
  // mode
  *mode = (short int)(byteArray[1] << 8 | byteArray[0]);
  // speed1
  *speed1 = (short int)(byteArray[3] << 8 | byteArray[2]);
  // speed2
  *speed2 = (short int)(byteArray[5] << 8 | byteArray[4]);
}

void send_packet(){
    toBytes(sendArray, mode);
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
    fromBytes(packetBuffer, &mode, &speed1, &speed2);
    Serial.println(mode);
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

// MOTION
void forward() {
  // set speed of movement
  analogWrite(enA, speed1 * factor);
  analogWrite(enB, speed2);

  // set both motors to forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void turn_right() {
  // set speed of movement
  analogWrite(enA, speed1 * factor);
  analogWrite(enB, 0);

  // set both motors to forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void turn_left() {
  // set speed of movement
  analogWrite(enA, 0);
  analogWrite(enB, speed2 * (1/factor));

  // set both motors to forward
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void stop() {
  analogWrite(enA, 0);
  analogWrite(enB, 0);

  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void update_time() {
  time_old = time_new;
  time_new = millis();
  dt = time_new - time_old;
}

void get_rpm() {
  static uint32_t previousMillis = millis();
  const short int pulsePerRotation = 20;
  if (time_new - previousMillis >= 1000) {
    rpm1 = (counter1 / pulsePerRotation) * 60;
    counter1 = 0;
    rpm2 = (60 * 1000/pulsePerRotation) / (time_new - previousMillis) * counter2;
    counter2 = 0;

    previousMillis= millis();
  }
}

void recv_serial(){
  if (Serial.available() > 0) {
    in_num= Serial.parseFloat();
    if (in_num > 2){
      if(in_num == 4 || in_num == 5 || in_num == 6 || in_num == 7){
        mode = in_num;
      }
    }else{
      factor = in_num;
    }
    Serial.println(in_num);
  }
}

void motion_call(){
  if (mode == 4){
    forward();
  }else if(mode == 5){
    turn_right();
  }else if(mode == 6){
    turn_left();
  }else if(mode == 7){
    stop();
  }
}

