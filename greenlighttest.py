import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GREEN_PIN_2 = 6

GPIO.setup(GREEN_PIN_2, GPIO.OUT)

GPIO.output(GREEN_PIN_2, GPIO.HIGH)
time.sleep(5)
GPIO.output(GREEN_PIN_2, GPIO.LOW)

GPIO.cleanup()
