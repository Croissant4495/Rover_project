// Motor A (left) connections
#define enA 5
#define in1 4
#define in2 3
// Motor B (right) connections
#define enB 9
#define in3 8
#define in4 7
// Encoder pins
#define encoder1 2;
#define encoder2 3;

//Variables
int counter1 = 0;
int rpm1 = 0;
int counter2 = 0;
int rpm2 = 0;

int desired_speed = 200;

int time_old;
int time_new;
float dt;
// want to move in straight line so both ultra sonic need to be equal
int error_1_diff_2_old;
int error_1_diff_2_new = 0;
float error_change;
long error_area = 0;
float correction_signal_1 = 0;
float correction_signal_2 = 0;

float k1 = 0.1;
float k2 = 70;
float k3 = 0.001;

// motor values
int speed1 = 150;
int speed2 = 150; 



//Functions declaration
void forward();
void stop();
void get_dist();

void update_time();
void update_error();
void update_correction();


void setup() {
  // Set all the motor control pins to outputs
	pinMode(enA, OUTPUT);
	pinMode(enB, OUTPUT);
	pinMode(in1, OUTPUT);
	pinMode(in2, OUTPUT);
	pinMode(in3, OUTPUT);
	pinMode(in4, OUTPUT);

  //set ultrasonic pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
	
	// Turn off motors - Initial state
	digitalWrite(in1, LOW);
	digitalWrite(in2, LOW);
	digitalWrite(in3, LOW);
	digitalWrite(in4, LOW);

  // 
  time_new = millis();

  Serial.begin(9600);

}


void loop() {
  //Main loop
  update_time();
  get_dist();
  update_error();
  update_correction();
  forward();
  // Serial.println(error_1_diff_2_new);
  // Serial.println(speed1);
  // Serial.println(speed2);
  delay(300);
}


void forward(){
  // set speed of movement
  analogWrite(enA, speed1);
  analogWrite(enB, speed2);

  // set both motors to forward
  digitalWrite(in1, HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3, HIGH);
  digitalWrite(in4, LOW);
}

void stop(){
  analogWrite(enA, 0);
  analogWrite(enB, 0);

  digitalWrite(in1, LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

void get_dist(){
    // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration_1 = pulseIn(echoPin, HIGH);
  // Calculating the distance
  distance_1= duration_1 * 0.034 / 2;

  // repeat for second sensor
  digitalWrite(trigPin2, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration_2 = pulseIn(echoPin2, HIGH);
  // Calculating the distance
  distance_2= duration_2 * 0.034 / 2;
  
}

void update_time(){
  time_old = time_new;
  time_new = millis();
  dt = time_new - time_old;
}


void update_error(){
  error_1_diff_2_old = error_1_diff_2_new;
  error_1_diff_2_new = distance_1 - distance_2;
  error_change = error_1_diff_2_new - error_1_diff_2_old;
  error_area = error_area + error_1_diff_2_new * dt;

}

void threshold(int* sp){
  if (*sp > 255){
    *sp = 255;
  }else if(*sp < 0){
    *sp = 0;
  }
}

void update_correction(){
  // // allow a 3cm range for error
  // if (abs(error_1_diff_2_new) < 3){
  //   speed1
  // }
  // -ve in speed1 because if distance 1 bigger than 2 (error positive) decrease speed of motor
  correction_signal_1 = k1 * -error_1_diff_2_new + k2 * (-error_change / dt) + k3 * -error_area;
  correction_signal_2 = k1 * error_1_diff_2_new + k2 * (error_change / dt) + k3 * error_area;
  Serial.print("Error:");
  Serial.println(correction_signal_1);
  Serial.println(correction_signal_2);
  speed1 = speed1 + correction_signal_1;
  // Serial.print("Speed1:");
  // Serial.println(speed1);
  threshold(&speed1);
  speed2 = speed2 + correction_signal_2;
  // Serial.print("Speed2:");
  // Serial.println(speed2);
  threshold(&speed2);
  
}