import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DATA_PIN = 16
CLOCK_PIN = 21
LATCH_PIN = 20

GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT)

def setOutput(ledpattern):
    GPIO.output(LATCH_PIN, 0)
    for x in range(16):
        GPIO.output(DATA_PIN, int(ledpattern[x]))
        GPIO.output(CLOCK_PIN, 1)
        GPIO.output(CLOCK_PIN, 0)
    
    GPIO.output(LATCH_PIN, 1)
    time.sleep(0.01)
    GPIO.output(LATCH_PIN, 0)

try:
    while True:
        setOutput("0000110110110110")
except KeyboardInterrupt:
    GPIO.cleanup()
