import RPi.GPIO as GPIO
import time

# Set up GPIO pin for the servo motor
servo_pin = 17  # GPIO17 (Pin 11)

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM on the servo pin at 50Hz (which is standard for most servos)
pwm = GPIO.PWM(servo_pin, 50)

# Start PWM with 0% duty cycle (so the servo stays still initially)
pwm.start(0)

def set_angle(angle):
    # Calculate the duty cycle for the specified angle (range: 0-180 degrees)
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)  # Wait for the servo to reach the position
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)

# Move the servo to 0 degrees
set_angle(0)
time.sleep(2)  # Wait for 2 seconds

# Move the servo to 90 degrees
set_angle(90)
time.sleep(2)

# Move the servo to 180 degrees
set_angle(180)
time.sleep(2)

# Cleanup
pwm.stop()
GPIO.cleanup()
