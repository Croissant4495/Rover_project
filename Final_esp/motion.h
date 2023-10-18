#ifndef _MOTION_H_
#define _MOTION_H_
//_________Definitions_________
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

//_________MOTION_VARIABLES_________
extern volatile unsigned int counter1;
extern int rpm1;
extern volatile unsigned int counter2;
extern int rpm2;
extern volatile unsigned long debounce;

extern long duration;
extern short int distance;

extern int time_old;
extern int time_new;
extern float dt;

extern short int mode;
extern short int gripper_mode;

// Motor values
extern float factor;
extern short int speed1;
extern short int speed2;

// Servo my_servo;

//_________Move_functions_________
void setup_pins();

void forward();
void stop();
void motion_call();

int get_dist();
void update_time();
void get_rpm();

//_________Interrupt_functions_________
// void IRAM_ATTR countPulse1();
// void IRAM_ATTR countPulse2();

#endif