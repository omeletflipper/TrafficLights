import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SOUND_SENSOR_PIN = 5
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def detect_sound():
    sound_detected = GPIO.input(SOUND_SENSOR_PIN)
    
    if sound_detected == 1:
        print("Sound detected")
    else:
        print("no sound detected")
    
try:
    while True:
        detect_sound()

except KeyboardInterrupt:
    GPIO.cleanup()
