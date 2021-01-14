import time
import RPi.GPIO as GPIO

# GPIO: General Purpose Input/Output ports.  

print(GPIO.VERSION)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins Motor 1
coil_A_1_pin = 24   # pink
coil_A_2_pin = 4    # orange
coil_B_1_pin = 23   # blau
coil_B_2_pin = 25   # gelb

# Pins Motor 2
coil2_A_1_pin = 18  # pink
coil2_A_2_pin = 22  # orange
coil2_B_1_pin = 17  # blau
coil2_B_2_pin = 27  # gelb

StepCount = 8

# Create a list from 0 to 7 (=8 items)
Seq = list(range(0, StepCount))

# Steuerungs-Schema um den Motor schrittweise weiterzubewegen
Seq[0] = [0,1,0,0]
Seq[1] = [0,1,0,1]
Seq[2] = [0,0,0,1]
Seq[3] = [1,0,0,1]
Seq[4] = [1,0,0,0]
Seq[5] = [1,0,1,0]
Seq[6] = [0,0,1,0]
Seq[7] = [0,1,1,0]

# Set GPIO mode (IN / OUT)
# Motor 1
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Motor 1
GPIO.setup(coil2_A_1_pin, GPIO.OUT)
GPIO.setup(coil2_A_2_pin, GPIO.OUT)
GPIO.setup(coil2_B_1_pin, GPIO.OUT)
GPIO.setup(coil2_B_2_pin, GPIO.OUT)


# Send power to the pins:
def setStep(w1, w2, w3, w4):
    # Push motor 1
    GPIO.output(coil_A_1_pin, w1)
    GPIO.output(coil_A_2_pin, w2)
    GPIO.output(coil_B_1_pin, w3)
    GPIO.output(coil_B_2_pin, w4)

    # Push motor 2
    GPIO.output(coil2_A_1_pin, w1)
    GPIO.output(coil2_A_2_pin, w2)
    GPIO.output(coil2_B_1_pin, w3)
    GPIO.output(coil2_B_2_pin, w4)


# Move forward
def forward(_delay, _steps):
    for i in range(_steps):
        for j in range(StepCount):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(_delay)


# Move backward
def backwards(_delay, _steps):
    for i in range(_steps):
        for j in reversed(range(StepCount)):
            setStep(Seq[j][0], Seq[j][1], Seq[j][2], Seq[j][3])
            time.sleep(_delay)


# 500 Schritte Vorwärts (eine Umdrehung)
delay = 1       # 1 millisecond is the maximum speed
steps = 500     # approx 1 round (360 degree)
forward(int(delay) / 1000.0, int(steps))

time.sleep(3)

# Halbe Umdrehung
delay = 1       # 1 millisecond is the maximum speed
steps = 250     # approx 1 round (360 degree)
forward(int(delay) / 1000.0, int(steps))

time.sleep(3)

# 2 Umdrehungen rückwärts
delay = 1
steps = 1000    # 2 Umdrehungen
backwards(int(delay) / 1000.0, int(steps))


print("Ready!")