import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# Set the gain (voltage range, default is ±4.096V)
ads.gain = 4

try:
    while True:
        # Read each channel
        chan0 = AnalogIn(ads, 0)  # Channel 0
        chan1 = AnalogIn(ads, 1)  # Channel 1
        chan2 = AnalogIn(ads, 2)  # Channel 2
        chan3 = AnalogIn(ads, 3)  # Channel 3

        # Print the voltage from each channel
        print(f"Channel 0: {chan0.voltage:.2f} V")
        print(f"Channel 1: {chan1.voltage:.2f} V")
        print(f"Channel 2: {chan2.voltage:.2f} V")
        print(f"Channel 3: {chan3.voltage:.2f} V")
        print("-" * 30)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Program terminated.")
