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
    for x in range(8):
        GPIO.output(DATA_PIN, int (ledpattern[x]))
        GPIO.output(CLOCK_PIN, 1)
        GPIO.output(CLOCK_PIN, 0)
    GPIO.output(LATCH_PIN, 1)

try:
    while True:
        setOutput("10000000")
        time.sleep(0.5)
        setOutput("01000000")
        time.sleep(0.5)
        setOutput("00100000")
        time.sleep(0.5)
        setOutput("00010000")
        time.sleep(0.5)
        setOutput("00001000")
        time.sleep(0.5)
        setOutput("00000100")
        time.sleep(0.5)
        setOutput("00000010")
        time.sleep(0.5)
        setOutput("00000001")
        time.sleep(0.5)
        setOutput("11111111")
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()  
