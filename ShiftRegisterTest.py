import RPi.GPIO as GPIO
import time

# Pin configuration
DATA = 16
CLOCK = 21
LATCH = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(DATA, GPIO.OUT)
GPIO.setup(CLOCK, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT)

def shift_out(data):
    GPIO.output(LATCH, GPIO.LOW)
    for bit in range(8):  # 8 bits for one shift register
        GPIO.output(CLOCK, GPIO.LOW)
        GPIO.output(DATA, GPIO.HIGH if (data & (1 << (7 - bit))) else GPIO.LOW)
        GPIO.output(CLOCK, GPIO.HIGH)
    GPIO.output(LATCH, GPIO.HIGH)
    time.sleep(0.05)  # Allow stabilization

try:
    while True:
        shift_out(0b11111111)
        time.sleep(2)
        shift_out(0b00000000)
        time.sleep(2)
        
except KeyboardInterrupt:
    GPIO.cleanup()
