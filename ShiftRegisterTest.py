import RPi.GPIO as GPIO
import time

# Pin configuration
DATA = 17
CLOCK = 27
LATCH = 22

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

try:
    while True:
        # Control Traffic Light LEDs
        shift_out(0b100)  # Turn on Red
        time.sleep(1)
        shift_out(0b010)  # Turn on Yellow
        time.sleep(1)
        shift_out(0b001)  # Turn on Green
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
