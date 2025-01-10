import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import soundfile as sf

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object with the I2C bus
ads = ADS.ADS1115(i2c)

# Set gain (you can adjust this if needed)
ads.gain = 1  # Gain = 1 (input voltage range ±4.096V)

# Create single-ended input on channel 0 (A0 pin)
chan0 = AnalogIn(ads, ADS.P0)

# Sampling rate and duration
sampling_rate = 44100  # 44.1 kHz sampling rate
duration = 5  # Record for 5 seconds

# Create an array to hold the recorded audio samples
audio_samples = []

# Record audio data for the specified duration
start_time = time.time()
while time.time() - start_time < duration:
    # Read voltage from the microphone sensor and append to audio_samples
    audio_samples.append(chan0.voltage)

# Write the recorded audio data to a .wav file
sf.write('recording3.wav', audio_samples, sampling_rate)

print("Recording saved as 'recording.wav'")
