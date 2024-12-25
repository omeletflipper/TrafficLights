import RPi.GPIO as GPIO
import time

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# GPIO pins for the first traffic light module
RED_PIN_1 = 18
YELLOW_PIN_1 = 23
GREEN_PIN_1 = 24

# GPIO pins for the second traffic light module
RED_PIN_2 = 16
YELLOW_PIN_2 = 26
GREEN_PIN_2 = 22

# GPIO pins for the third traffic light module
RED_PIN_3 = 27
YELLOW_PIN_3 = 17
GREEN_PIN_3 = 4

# GPIO pins for the fourth traffic light module
RED_PIN_4 = 19
YELLOW_PIN_4 = 21
GREEN_PIN_4 = 20

# Setup GPIO pins as output
for pin in [
    RED_PIN_1, YELLOW_PIN_1, GREEN_PIN_1,
    RED_PIN_2, YELLOW_PIN_2, GREEN_PIN_2,
    RED_PIN_3, YELLOW_PIN_3, GREEN_PIN_3,
    RED_PIN_4, YELLOW_PIN_4, GREEN_PIN_4
]:
    GPIO.setup(pin, GPIO.OUT)

# Functions to turn on each light for a specific module
def red_on(module):
    if module == 1:
        GPIO.output(RED_PIN_1, GPIO.HIGH)
        GPIO.output(YELLOW_PIN_1, GPIO.LOW)
        GPIO.output(GREEN_PIN_1, GPIO.LOW)
    elif module == 2:
        GPIO.output(RED_PIN_2, GPIO.HIGH)
        GPIO.output(YELLOW_PIN_2, GPIO.LOW)
        GPIO.output(GREEN_PIN_2, GPIO.LOW)
    elif module == 3:
        GPIO.output(RED_PIN_3, GPIO.HIGH)
        GPIO.output(YELLOW_PIN_3, GPIO.LOW)
        GPIO.output(GREEN_PIN_3, GPIO.LOW)
    elif module == 4:
        GPIO.output(RED_PIN_4, GPIO.HIGH)
        GPIO.output(YELLOW_PIN_4, GPIO.LOW)
        GPIO.output(GREEN_PIN_4, GPIO.LOW)

def yellow_on(module):
    if module == 1:
        GPIO.output(RED_PIN_1, GPIO.LOW)
        GPIO.output(YELLOW_PIN_1, GPIO.HIGH)
        GPIO.output(GREEN_PIN_1, GPIO.LOW)
    elif module == 2:
        GPIO.output(RED_PIN_2, GPIO.LOW)
        GPIO.output(YELLOW_PIN_2, GPIO.HIGH)
        GPIO.output(GREEN_PIN_2, GPIO.LOW)
    elif module == 3:
        GPIO.output(RED_PIN_3, GPIO.LOW)
        GPIO.output(YELLOW_PIN_3, GPIO.HIGH)
        GPIO.output(GREEN_PIN_3, GPIO.LOW)
    elif module == 4:
        GPIO.output(RED_PIN_4, GPIO.LOW)
        GPIO.output(YELLOW_PIN_4, GPIO.HIGH)
        GPIO.output(GREEN_PIN_4, GPIO.LOW)

def green_on(module):
    if module == 1:
        GPIO.output(RED_PIN_1, GPIO.LOW)
        GPIO.output(YELLOW_PIN_1, GPIO.LOW)
        GPIO.output(GREEN_PIN_1, GPIO.HIGH)
    elif module == 2:
        GPIO.output(RED_PIN_2, GPIO.LOW)
        GPIO.output(YELLOW_PIN_2, GPIO.LOW)
        GPIO.output(GREEN_PIN_2, GPIO.HIGH)
    elif module == 3:
        GPIO.output(RED_PIN_3, GPIO.LOW)
        GPIO.output(YELLOW_PIN_3, GPIO.LOW)
        GPIO.output(GREEN_PIN_3, GPIO.HIGH)
    elif module == 4:
        GPIO.output(RED_PIN_4, GPIO.LOW)
        GPIO.output(YELLOW_PIN_4, GPIO.LOW)
        GPIO.output(GREEN_PIN_4, GPIO.HIGH)


# Main loop for cycling through the lights
try:
    while True:
        for module in [1, 2, 3, 4]:
            
            
            #light 1
            green_on(1)
            red_on(2)
            red_on(3)
            red_on(4)
            time.sleep(5)
            yellow_on(1)
            time.sleep(1)
            
            #light 2
            green_on(2)
            red_on(1)
            red_on(3)
            red_on(4)
            time.sleep(5)
            yellow_on(1)
            time.sleep(1)
            
            #light 3
            red_on(1)
            red_on(2)
            green_on(3)
            red_on(4)
            time.sleep(5)
            yellow_on(3)
            time.sleep(1)
 
            #light 4
            red_on(1)
            red_on(2)
            red_on(3)
            green_on(4)
            time.sleep(5)
            yellow_on(4)
            time.sleep(1)
            
except KeyboardInterrupt:
    GPIO.cleanup()
