import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate input signal
t = np.linspace(0, 1, 200)
x = np.sin(2 * np.pi * 5 * t)

# Step 2: Initialize
predicted = np.zeros(len(x))
error = np.zeros(len(x))
quantized_error = np.zeros(len(x))
reconstructed = np.zeros(len(x))

step_size = 0.2

# Initialize first sample
reconstructed[0] = x[0]

# ==============================
# DPCM MODULATION (ENCODING)
# ==============================
for i in range(1, len(x)):
    predicted[i] = reconstructed[i-1]
    error[i] = x[i] - predicted[i]
    quantized_error[i] = step_size * np.round(error[i] / step_size)

# ==============================
# DPCM DEMODULATION (DECODING)
# ==============================
for i in range(1, len(x)):
    reconstructed[i] = reconstructed[i-1] + quantized_error[i]

# ==============================
# Plot 1: Original Signal
# ==============================
plt.figure(figsize=(8,4))
plt.plot(t, x)
plt.title("Original Input Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


# ==============================
# Plot 2: DPCM Modulation (Error Signal)
# ==============================
plt.figure(figsize=(8,4))
plt.plot(t, error)
plt.title("DPCM Modulated Signal (Prediction Error)")
plt.xlabel("Time")
plt.ylabel("Error")
plt.grid()


# ==============================
# Plot 3: Quantized Signal
# ==============================
plt.figure(figsize=(8,4))
plt.plot(t, quantized_error)
plt.title("Quantized Error Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


# ==============================
# Plot 4: DPCM Demodulated Signal
# ==============================
plt.figure(figsize=(8,4))
plt.plot(t, x, label="Original Signal")
plt.plot(t, reconstructed, '--', label="Demodulated Signal")
plt.title("DPCM Demodulation (Reconstructed Signal)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()