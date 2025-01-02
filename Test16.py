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
    """
    Send a 16-bit pattern to the shift registers.
    """
    GPIO.output(LATCH_PIN, 0)
    for x in range(16):  # Adjusted for 16 bits
        GPIO.output(DATA_PIN, int(ledpattern[x]))  # Send bit by bit
        GPIO.output(CLOCK_PIN, 1)  # Pulse clock
        GPIO.output(CLOCK_PIN, 0)
    GPIO.output(LATCH_PIN, 1)  

try:
    while True:
        setOutput("0000000000010000")
        time.sleep(0.5)
        setOutput("0000000000100000")
        time.sleep(0.5)
        setOutput("0000000001000000")
        time.sleep(0.5)
        setOutput("0000000010000000")
        time.sleep(0.5)
        setOutput("0000000001000000")
        time.sleep(0.5)
        setOutput("0000000000100000")
        time.sleep(0.5)
        setOutput("0000000000010000")
        time.sleep(0.5)
        setOutput("0000000000001000")
        time.sleep(0.5)
        setOutput("0000000000000100")
        time.sleep(0.5)
        setOutput("0000000000000010")
        time.sleep(0.5)
        setOutput("0000000000000001")
        time.sleep(0.5)
        setOutput("1111111111111111") #all on
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()