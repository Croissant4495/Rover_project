float my_float;
void recieve();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("<ESP is ready>");
}

void loop() {
  // put your main code here, to run repeatedly:
  recieve();
  Serial.println("Other code");
}

void recieve() {
  if (Serial.available() > 0) {
    my_float= Serial.parseFloat();
    Serial.println(my_float);
  }
}






