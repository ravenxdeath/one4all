#include <AFMotor.h>

// Create the motor shield object with the default I2C address
AF_DCMotor motor1(1); // Motor M1
AF_DCMotor motor2(4); // Motor M4

void setup() {
  // Set up serial connection for debugging
  Serial.begin(9600);
  Serial.println("Serial connection initialized.");

  // Set speed for the motors
  motor1.setSpeed(255);
  motor2.setSpeed(255);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    Serial.print("Received command: ");
    Serial.println(command);

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
  delay(2000); // Move forward for 2 seconds
  stopMotors();
}

void moveBackward() {
  Serial.println("Moving backward.");
  motor1.run(BACKWARD);
  motor2.run(BACKWARD);
  delay(2000); // Move backward for 2 seconds
  stopMotors();
}

void turnLeft() {
  Serial.println("Turning left.");
  motor1.run(BACKWARD);
  motor2.run(FORWARD);
  delay(2000); // Turn left for 2 seconds
  stopMotors();
}

void turnRight() {
  Serial.println("Turning right.");
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  delay(2000); // Turn right for 2 seconds
  stopMotors();
}

void stopMotors() {
  Serial.println("Stopping.");
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}
