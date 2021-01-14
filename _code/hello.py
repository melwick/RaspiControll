import time
import RPi.GPIO as GPIO

# GPIO: General Purpose Input/Output ports

print("Hello")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set IO Mode (IN/OUT)
GPIO.setup(23,GPIO.OUT)
print("LED on")

GPIO.output(23,GPIO.HIGH)

# Wait for 5 seconds
time.sleep(5)

print("LED off")
GPIO.output(23,GPIO.LOW)