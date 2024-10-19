#include <AFMotor.h>
#include <SoftwareSerial.h>
#include <Servo.h>

SoftwareSerial BTSerial(2, 3); // RX, TX, connected to pins 2 and 3 on Arduino Uno

// Create the motor shield object with the default I2C address
AF_DCMotor motor1(1); // Motor M1
AF_DCMotor motor2(4); // Motor M4

Servo servoMotor; // Create a servo object to control the servo motor
int servoPin = 9; // Define the pin connected to the servo motor

const int trigPin = 6; // Pin connected to the ultrasonic sensor's trigger pin
const int echoPin = 7; // Pin connected to the ultrasonic sensor's echo pin

unsigned long lastCheckTime = 0; // Variable to store the time of the last obstacle check
const unsigned long checkInterval = 5000; // Interval between obstacle checks (milliseconds)

void setup() {
  // Set up serial connection for debugging
  Serial.begin(9600);
  Serial.println("Serial connection initialized.");

  // Set up Bluetooth serial connection
  BTSerial.begin(9600);
  Serial.println("Bluetooth connection initialized.");

  // Set up servo motor
  servoMotor.attach(servoPin);
  Serial.println("Servo motor initialized.");

  // Set up ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Set speed for the motors
  motor1.setSpeed(255);
  motor2.setSpeed(255);
}

void loop() {
  if (BTSerial.available()) {
    char command = BTSerial.read();
    if (command == 'F') {
      checkAndMoveForward();
    } else if (command == 'B') {
      checkAndMoveBackward();
    } else if (command == 'L') {
      checkAndTurnLeft();
    } else if (command == 'R') {
      checkAndTurnRight();
    } else if (command == 'S') {
      stopMotors();
    }
  }
  
  // Check if it's time to perform obstacle detection
  unsigned long currentTime = millis();
  if (currentTime - lastCheckTime >= checkInterval) {
    lastCheckTime = currentTime;
    checkAndAvoidObstacle();
  }
}

void checkAndMoveForward() {
  if (!isObstacleDetected()) {
    moveForward();
  } else {
    stopMotors();
    checkAndAvoidObstacle();
  }
}

void checkAndMoveBackward() {
  if (!isObstacleDetected()) {
    moveBackward();
  } else {
    stopMotors();
    checkAndAvoidObstacle();
  }
}

void checkAndTurnLeft() {
  if (!isObstacleDetected()) {
    turnLeft();
  } else {
    stopMotors();
    checkAndAvoidObstacle();
  }
}

void checkAndTurnRight() {
  if (!isObstacleDetected()) {
    turnRight();
  } else {
    stopMotors();
    checkAndAvoidObstacle();
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
  delay(1000); // Adjust delay based on required turn angle
}

void turnRight() {
  Serial.println("Turning right.");
  motor1.run(FORWARD);
  motor2.run(BACKWARD);
  delay(1000); // Adjust delay based on required turn angle
}

void stopMotors() {
  Serial.println("Stopping.");
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}

bool isObstacleDetected() {
  // Trigger ultrasonic sensor to send a pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Read the pulse from the echo pin
  long duration = pulseIn(echoPin, HIGH);
  
  // Convert the pulse duration to distance in centimeters
  int distance = duration * 0.034 / 2;

  // Check if obstacle is detected within threshold distance
  return distance < 5; // Adjust threshold distance as needed
}

void checkAndAvoidObstacle() {
  Serial.println("Checking for obstacle...");

  if (isObstacleDetected()) {
    Serial.println("Obstacle detected. Avoiding.");
    
    // Rotate the servo to scan for a clear path
    for (int angle = 45; angle <= 135; angle += 15) {
      servoMotor.write(angle);
      delay(500); // Adjust delay based on servo speed
      if (!isObstacleDetected()) {
        // If a clear path is found, turn in that direction and exit the loop
        if (angle <= 90) {
          turnLeft();
        } else {
          turnRight();
        }
        return;
      }
    }

    // If no clear path is found, turn around
    turnLeft();
    delay(1000); // Adjust delay based on required turn angle
  } else {
    Serial.println("No obstacle detected. Resuming movement.");
    moveForward(); // Resume forward movement
  }
}
