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
        setOutput("0000001001001100")
        time.sleep(3)
        setOutput("0000001001001010")
        time.sleep(1)
        setOutput("0000001001001001")
    
        setOutput("0000001001100001")
        time.sleep(3)
        setOutput("0000001001010001")
        time.sleep(1)
        setOutput("0000001001001001")
        
        setOutput("0000001100001001")
        time.sleep(3)
        setOutput("0000001010001001")
        time.sleep(1)
        setOutput("0000001001001001")
        
        setOutput("0000100001001001")
        time.sleep(3)
        setOutput("0000010001001001")
        time.sleep(1)
        setOutput("0000001001001001")
        
        
except KeyboardInterrupt:
    GPIO.cleanup()
