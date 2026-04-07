#  Unipolar RZ (Return to Zero) Signal Generation

import numpy as np
import matplotlib.pyplot as plt

bits = np.array([1, 0, 1, 1, 0, 0, 1])
samples_per_bit = 100

rz_signal = []

for bit in bits:
    if bit == 1:
        first_half = np.ones(samples_per_bit//2)
        second_half = np.zeros(samples_per_bit//2)
    else:
        first_half = np.zeros(samples_per_bit//2)
        second_half = np.zeros(samples_per_bit//2)
    
    rz_signal.extend(first_half)
    rz_signal.extend(second_half)

rz_signal = np.array(rz_signal)
t = np.arange(len(rz_signal))

plt.figure(figsize=(10,3))
plt.plot(t, rz_signal)
plt.title("Unipolar RZ Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()