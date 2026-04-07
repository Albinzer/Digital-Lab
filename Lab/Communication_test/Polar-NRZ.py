#  Polar NRZ (Non-Return to Zero) Signal Generation

import numpy as np
import matplotlib.pyplot as plt

bits = np.array([1, 0, 1, 1, 0, 0, 1])
samples_per_bit = 100

# Mapping: 1 → +1, 0 → -1
signal = 2*bits - 1

# Create waveform
polar_nrz = np.repeat(signal, samples_per_bit)

t = np.arange(len(polar_nrz))

plt.figure(figsize=(10,3))
plt.plot(t, polar_nrz)
plt.title("Polar NRZ Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()