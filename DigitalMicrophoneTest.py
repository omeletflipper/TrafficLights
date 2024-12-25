import RPi.GPIO as GPIO
import time

MIC_PIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(MIC_PIN, GPIO.IN)

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(MIC_PIN) == GPIO.HIGH:  # Sound detected
            print("Sound detected")
        else:
            print("No sound")


except KeyboardInterrupt:
    GPIO.cleanup()
