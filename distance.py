#!/usr/bin/env python
import RPi.GPIO as gpio
import time
import sys
import signal

# Handle Ctrl+C to exit cleanly
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    gpio.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# GPIO Mode
gpio.setmode(gpio.BCM)

# Define pins for Sensor 1
trig1 = 23
echo1 = 18

# Define pins for Sensor 2
trig2 = 20
echo2 = 21

# Set up GPIO
gpio.setup(trig1, gpio.OUT)
gpio.setup(echo1, gpio.IN)
gpio.setup(trig2, gpio.OUT)
gpio.setup(echo2, gpio.IN)

time.sleep(0.5)
print('-----------------------------------------------------------------sonar start')

# Function to measure distance
def measure_distance(trig, echo):
    gpio.output(trig, False)
    time.sleep(0.1)
    gpio.output(trig, True)
    time.sleep(0.00001)
    gpio.output(trig, False)

    try:
        while gpio.input(echo) == 0:
            pulse_start = time.time()
        while gpio.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000

        # Timeout and range validation
        if distance >= 0.01746:
            return 'timeout'
        elif distance > 10 or distance == 0:
            return 'out of range'

        return round(distance, 3)
    except:
        return 'error'

# Main loop
try:
    while True:
        # Measure distance for Sensor 1
        distance1 = measure_distance(trig1, echo1)

        # Measure distance for Sensor 2
        distance2 = measure_distance(trig2, echo2)

        # Print distances
        print(f"Sensor 1 Distance: {distance1}")
        print(f"Sensor 2 Distance: {distance2}")

        # Check if one is timeout but the other is valid
        if distance1 == 'timeout' and isinstance(distance2, (int, float)):
            print("Sensor 1 timeout, but Sensor 2 is valid: ", distance2)
        elif distance2 == 'timeout' and isinstance(distance1, (int, float)):
            print("Sensor 2 timeout, but Sensor 1 is valid: ", distance1)

except (KeyboardInterrupt, SystemExit):
    gpio.cleanup()
    sys.exit(0)
except Exception as e:
    print(f"An error occurred: {e}")
    gpio.cleanup()
