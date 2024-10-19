#include <AFMotor.h>
#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial BTSerial(2, 3); // RX, TX, connected to pins 2 and 3 on Arduino Uno
Servo ultrasoundServo; // Define the servo object

// Create the motor shield object with the default I2C address
AF_DCMotor motor1(1); // Motor M1
AF_DCMotor motor2(4); // Motor M4

const int trigPin = 6; // Pin connected to the ultrasonic sensor's trigger pin
const int echoPin = 7;
long duration;
int distance;

void setup() {
  // Set up serial communication with a baud rate of 9600
  BTSerial.begin(9600);

  // Set up motors
  motor1.setSpeed(255);
  motor2.setSpeed(255);

  // Set up the servo
  ultrasoundServo.attach(9); // Attach the servo to pin 9
}

void loop() {
  if (BTSerial.available()) {
    char command = BTSerial.read(); // Read the incoming command from Bluetooth

    // Perform action based on the received command
    switch (command) {
      case 'F': // Forward
        forward();
        break;
      case 'B': // Backward
        backward();
        break;
      case 'L': // Left-forward
        leftForward();
        break;
      case 'R': // Right-forward
        rightForward();
        break;
      case 'S': // Stop
        stop();
        break;
    }
  }

  // Rotate the ultrasonic sensor to scan for obstacles
  for (int angle = 0; angle <= 180; angle += 10) {
    ultrasoundServo.write(angle); // Rotate the servo to the current angle
    delay(500); // Wait for the servo to reach the position

    // Measure the distance using ultrasonic sensor
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    duration = pulseIn(echoPin, HIGH);
    distance = duration * 0.034 / 2;

    // Check if obstacle is detected
    if (distance < 20) { // Adjust this threshold as needed
      // Perform an action to avoid the obstacle
      // For example, stop and turn
      stop();
      delay(500); // Stop for a moment
      // Choose appropriate avoidance action here
    }
  }
}

void forward() {
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}

void backward() {
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
}

void leftForward() {
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  delay(500); // Adjust this delay according to the time needed for the turn
  forward(); // Move forward after turning left
}

void rightForward() {
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  delay(500);
  forward();
}

void stop() {
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}
