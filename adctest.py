import time
import board
import busio
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)

# Set up single-ended channels for each KY 037 (A0, A1, A2, A3)
mic_1 = AnalogIn(ads, ADS1115.P0)  # KY-037 A0 to ADS1115 A0
mic_2 = AnalogIn(ads, ADS1115.P1)  # KY-037 A0 to ADS1115 A1
mic_3 = AnalogIn(ads, ADS1115.P2)  # KY-037 A0 to ADS1115 A2
mic_4 = AnalogIn(ads, ADS1115.P3)  # KY-037 A0 to ADS1115 A3

# Loop
try:
    while True:
        print(f"Mic 1 Voltage: {mic_1.voltage:.2f} V")
        print(f"Mic 2 Voltage: {mic_2.voltage:.2f} V")
        print(f"Mic 3 Voltage: {mic_3.voltage:.2f} V")
        print(f"Mic 4 Voltage: {mic_4.voltage:.2f} V")
        print("-" * 30)
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping")
