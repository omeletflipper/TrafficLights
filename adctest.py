import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# Initialize I2C bus and ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# Set the gain (voltage range, default is 2/3 for ±6.144V range)
ads.gain = 1  # ±4.096V range

try:
    while True:
        mic1 = AnalogIn(ads, ADS1115.P0)
        mic2 = AnalogIn(ads, ADS1115.P1)
        mic3 = AnalogIn(ads, ADS1115.P2)
        mic4 = AnalogIn(ads, ADS1115.P3)

        # Read and print the voltage for each channel
        print(f"Channel 0: {mic1.voltage:.2f} V")
        print(f"Channel 1: {mic2.voltage:.2f} V")
        print(f"Channel 2: {mic3.voltage:.2f} V")
        print(f"Channel 3: {mic4.voltage:.2f} V")
        print("-" * 30)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Program terminated.")
