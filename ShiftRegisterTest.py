import RPi.GPIO as GPIO
import time

# Define GPIO pins for shift register
data_pin = 16  # DS pin
clock_pin = 21  # SHCP pin
latch_pin = 20  # STCP pin

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(data_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)

# Function to send data to the shift register
def shift_out(data):
    for bit in range(8):
        GPIO.output(data_pin, (data >> (7 - bit)) & 1)
        GPIO.output(clock_pin, GPIO.HIGH)
        GPIO.output(clock_pin, GPIO.LOW)

def latch_data():
    GPIO.output(latch_pin, GPIO.HIGH)
    GPIO.output(latch_pin, GPIO.LOW)


try:
    while True:
        shift_out(0b11111111)  # 0xFF = 11111111 in binary (turn on all LEDs)
        latch_data()
        time.sleep(1)  
        shift_out(0b00000000)
        latch_data()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()  
