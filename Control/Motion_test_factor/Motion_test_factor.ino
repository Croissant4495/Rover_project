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
float factor = 0.4;
int speed1 = 230;
int speed2 = 230;

// input reader
float in_num = 0;
// mode
int mode = 4;


//Functions declaration
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


// union to use float as byte
typedef union {
  float floatingPoint;
  byte binary[4];
} binaryFloat;

void setup() {
  // Set all the motor control pins to outputs
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  //set encoder pins
  pinMode(encoder1, INPUT_PULLUP);
  pinMode(encoder2, INPUT_PULLUP);
  attachInterrupt(encoder1, countPulse1, RISING);
  attachInterrupt(encoder2, countPulse2, RISING);

  // Turn off motors - Initial state
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);

  time_new = millis();

  Serial.begin(9600);
}


void loop() {
  //Main loop
  update_time();
  noInterrupts();
  get_rpm();
  interrupts();
  recv_serial();
  // Serial.print("Motor 1:");
  // Serial.println(rpm1);
  Serial.print("Motor 2:");
  Serial.println(rpm2);
  motion_call();

  delay(300);
}


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
