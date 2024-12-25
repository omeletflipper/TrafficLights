import RPi.GPIO as GPIO
import time

MIC_PIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(MIC_PIN, GPIO.IN)

try:
    while True:
        if GPIO.input(MIC_PIN) == GPIO.HIGH:  # Sound detected
            print("Sound detected!")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
