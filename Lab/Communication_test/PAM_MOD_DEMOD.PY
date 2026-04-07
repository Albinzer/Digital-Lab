# lab 5

import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_bits = 20
samples_per_bit = 100
amplitude = 5

# Generate random binary data
bits = np.random.randint(0, 2, num_bits)

# PAM Mapping: 0 -> -A, 1 -> +A
pam_symbols = np.where(bits == 1, amplitude, -amplitude)

# Upsample (modulated signal)
pam_signal = np.repeat(pam_symbols, samples_per_bit)

# Time axis
t = np.arange(len(pam_signal)) / samples_per_bit

# Add noise
noise = np.random.normal(0, 1, len(pam_signal))
received_signal = pam_signal + noise

# Demodulation
sample_points = np.arange(samples_per_bit//2, len(received_signal), samples_per_bit)
sampled_values = received_signal[sample_points]

# Decision rule
recovered_bits = (sampled_values > 0).astype(int)

# Demodulated waveform
demod_symbols = np.where(recovered_bits == 1, amplitude, -amplitude)
demod_signal = np.repeat(demod_symbols, samples_per_bit)

# Plotting
plt.figure(figsize=(10, 10))

# 1. Original Bits
plt.subplot(4,1,1)
plt.step(np.arange(len(bits)), bits, where='post')
plt.title("Original Binary Signal")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid()

# 2. PAM Modulated Signal
plt.subplot(4,1,2)
plt.plot(t, pam_signal)
plt.title("PAM Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

# 3. Received Signal (with Noise)
plt.subplot(4,1,3)
plt.plot(t, received_signal)
plt.scatter(sample_points/samples_per_bit, sampled_values, color='red')
plt.title("Received Signal with Noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

# 4. Demodulated Signal
plt.subplot(4,1,4)
plt.plot(t, demod_signal)
plt.title("Demodulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


plt.tight_layout()
plt.show()