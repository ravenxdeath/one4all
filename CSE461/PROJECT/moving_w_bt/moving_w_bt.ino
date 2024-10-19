#include <AFMotor.h>
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(2, 3); // RX, TX, connected to pins 2 and 3 on Arduino Uno

// Create the motor shield object with the default I2C address
AF_DCMotor motor1(1); // Motor M1
AF_DCMotor motor2(4); // Motor M4

void setup() {
  // Set up serial connection for debugging
  Serial.begin(9600);
  Serial.println("Serial connection initialized.");

  // Set up Bluetooth serial connection
  BTSerial.begin(9600);
  Serial.println("Bluetooth connection initialized.");

  // Set speed for the motors
  motor1.setSpeed(255);
  motor2.setSpeed(255);
}

void loop() {
  // Check if Bluetooth data is available
  if (BTSerial.available()) {
    char command = BTSerial.read();
    Serial.print("Received command: ");
    Serial.println(command);
    
    // Perform action based on command received
    switch (command) {
      case 'F':
        moveForward();
        break;
      case 'B':
        moveBackward();
        break;
      case 'L':
        turnLeft();
        break;
      case 'R':
        turnRight();
        break;
      case 'A':
        moveLeft();
        break;
      case 'D':
        moveRight();
        break;
      case 'S':
        stopMotors();
        break;
      default:
        Serial.println("Invalid command.");
        break;
    }
  }
}

void moveForward() {
  Serial.println("Moving forward.");
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}

void moveBackward() {
  Serial.println("Moving backward.");
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
}

void turnLeft() {
  Serial.println("Turning left.");
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
}

void turnRight() {
  Serial.println("Turning right.");
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
}

void moveLeft() {
  Serial.println("Moving left.");
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  // Adjust delay or additional logic if needed
}

void moveRight() {
  Serial.println("Moving right.");
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  // Adjust delay or additional logic if needed
}

void stopMotors() {
  Serial.println("Stopping.");
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}
