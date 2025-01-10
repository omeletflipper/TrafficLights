import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import wave
import numpy as np

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object with the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0 (A0)
chan = AnalogIn(ads, ADS.P0)

# Recording settings
sample_rate = 8000  # Samples per second
record_time = 6  # Duration of recording in seconds
output_file = "recording2.wav"

# WAV file setup
wav_file = wave.open(output_file, "w")
wav_file.setnchannels(1)  # Mono
wav_file.setsampwidth(2)  # 16-bit audio
wav_file.setframerate(sample_rate)

# Recording loop
print(f"Recording for {record_time} seconds...")
start_time = time.time()
samples = []

while time.time() - start_time < record_time:
    # Read the voltage from the ADS1115
    voltage = chan.voltage
    # Convert to 16-bit integer (-32768 to 32767)
    int_value = int((voltage / 4.096) * 32767)  # Assuming 4.096V reference
    samples.append(int_value)
    time.sleep(1 / sample_rate)  # Wait for the next sample

# Save the samples to a WAV file
wav_data = np.array(samples, dtype=np.int16)
wav_file.writeframes(wav_data.tobytes())
wav_file.close()

print(f"Recording saved to {output_file}")
