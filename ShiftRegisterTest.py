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
    time.sleep(0.05)  # Allow stabilization

try:
    while True:
        print("Red ON")
        shift_out(0b00000001)  # Red LED
        time.sleep(1)

        print("Yellow ON")
        shift_out(0b00000010)  # Yellow LED
        time.sleep(1)

        print("Green ON")
        shift_out(0b00000100)  # Green LED
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
