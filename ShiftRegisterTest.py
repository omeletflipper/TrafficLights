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

# Function to send data to the shift registers (16 bits)
def shift_out(data):
    for bit in range(16):  # 16 bits for 2 shift registers
        # Send one bit at a time
        GPIO.output(data_pin, (data >> (15 - bit)) & 1)
        GPIO.output(clock_pin, GPIO.HIGH)
        GPIO.output(clock_pin, GPIO.LOW)

# Function to latch the data (activate LEDs)
def latch_data():
    GPIO.output(latch_pin, GPIO.HIGH)
    GPIO.output(latch_pin, GPIO.LOW)


try:
    while True:
        shift_out(0b1111111111111111) 
        latch_data()
        time.sleep(1)  
        shift_out(0b0000000000000000)
    
except KeyboardInterrupt:
    GPIO.cleanup()  
