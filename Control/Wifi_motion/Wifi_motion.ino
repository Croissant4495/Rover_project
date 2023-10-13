//_________Libraries_________
#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

//_________Definitions_________
// WIFI
#define rcv_message_length 6

// Motor A (left) connections
#define enA 21
#define in1 19
#define in2 5
// Motor B (right) connections
#define enB 23
#define in3 18
#define in4 22
// Encoder pins
#define encoder1 34
#define encoder2 35
// Servo pin
#define servo 18
//Ultrasonic connections
#define trigPin 4
#define echoPin 2


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
static volatile unsigned long debounce = 0;

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

//_________WIFI_functions_________
void toBytes(unsigned char *byteArray, short int var1);
void fromBytes(unsigned char *byteArray, short int* var1, short int* var2, short int* var3, short int* var4);
void start_server();

void send_packet();
void recv_bytes(WiFiClient* client_ptr);

//_________Move_functions_________
void forward();
void stop();
int get_dist();

void update_time();
void get_rpm();

//_________Interrupt_functions_________
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

  // pinMode(servo, OUTPUT);
  // my_servo.attach(servo);

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

  Serial.begin(115200);
  Serial.print("Started program");
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
        recv_bytes(&client);
        client.flush();
      }
      motion_call();
    }
    Serial.println("Client dissconnected");
  }else{
    stop();
  }
}

// _________WIFI_________
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
    toBytes(sendArray, mode);
}

void recv_bytes(WiFiClient* client_ptr){
  for (int i = 0; i<= rcv_message_length; i++){
    packetBuffer[i] = client_ptr->read();
    }
  fromBytes(packetBuffer, &mode, &speed1, &speed2, &gripper_mode);
  Serial.print("Mode: ");
  Serial.println(mode);
  Serial.print("Speed1: ");
  Serial.println(speed1);
  Serial.print("Speed2: ");
  Serial.println(speed2);
  Serial.print("Gripper_mode: ");
  Serial.println(gripper_mode);
}

//_________MOTION_________
void forward() {
  // set speed of movement
  analogWrite(enA, speed1);
  analogWrite(enB, speed2);

  // set both motors to forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void turn_right() {
  // set speed of movement
  analogWrite(enA, speed1);
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
  analogWrite(enB, speed2);

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

int get_dist(){
    // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance = duration * 0.034 / 2;
  return distance;
}

// void move_servo(int speed){
//   my_servo.write(speed)
// }
void motion_call(){
  if (mode == 1){
    forward();
  }else if(mode == 2){
    turn_right();
  }else if(mode == 3){
    turn_left();
  }else if(mode == 0){
    stop();
  }

  // if (gripper_mode == 2){
  //   move_servo(135);
  // }else if(gripper_mode == 1){
  //   move_servo(45);
  // }else{
  //   move_servo(90);
  // }
}

