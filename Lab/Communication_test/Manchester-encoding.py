import numpy as np
import matplotlib.pyplot as plt

# Step 1: Input bits
bits = np.array([1, 0, 1, 1, 0, 0, 1])

# Step 2: Manchester encoding
samples_per_bit = 100
manchester_signal = []

for bit in bits:
    if bit == 1:
        # High → Low
        first_half = np.ones(samples_per_bit//2)
        second_half = -1 * np.ones(samples_per_bit//2)
    else:
        # Low → High
        first_half = -1 * np.ones(samples_per_bit//2)
        second_half = np.ones(samples_per_bit//2)
    
    manchester_signal.extend(first_half)
    manchester_signal.extend(second_half)

manchester_signal = np.array(manchester_signal)

# Time axis
t = np.arange(len(manchester_signal))

# Step 3: Plot
plt.figure(figsize=(12,4))
plt.plot(t, manchester_signal)
plt.title("Manchester Encoded Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.show()

# Output bits
print("Input Bits:", bits)