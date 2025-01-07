import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from gpiozero import DigitalInputDevice

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object with the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended inputs on the channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

delayTime = 1
# Initialize the DigitalInputDevice for the sensor at GPIO 24
digital_pin = DigitalInputDevice(4, pull_up=False)  # pull_up=False, because pull_up_down=GPIO.PUD_OFF

while True:
    analog = '%.2f' % chan0.voltage

    # Output to the console
    if not digital_pin.is_active:
        print("Analog voltage value:", analog, "V, ", "Limit value: not yet reached")
    else:
        print("Analog voltage value:", analog, "V, ", "Limit value: reached")
        print("---------------------------------------")

    # Reset + Delay
    time.sleep(delayTime)
