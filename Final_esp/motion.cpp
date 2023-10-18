#include "motion.h"

void setup_pins(){
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
}

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

// void IRAM_ATTR countPulse1() {
//   counter1++;
// }

// void IRAM_ATTR countPulse2() {
//   if(  digitalRead (encoder2) && (micros()-debounce > 500) && digitalRead (encoder2) ) { 
//         debounce = micros();
//         counter2 ++;
//       }
//         else ; 
// }