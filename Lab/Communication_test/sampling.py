import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Continuous signal
t_cont = np.linspace(0, 1, 1000)                                                # np.linspace(start, stop, num)
f = 5
x_cont = np.sin(2 * np.pi * f * t_cont)                                          # x(t) = sin(2π f t) --sin _ wave formula

# Sampling
fs = 20
t_sample = np.arange(0, 1, 1/fs)
x_sample = np.sin(2 * np.pi * f * t_sample)                                     # sampled signal

# Reconstruction (FIX APPLIED)                                        # communication flow:  Analog → Sampling → Digital → Transmission → Reconstruction → Analog =====why we need reconstruct
reconstruct = interp1d(t_sample, x_sample, kind='cubic')
t_recon = np.linspace(0, t_sample.max(), 1000)
x_recon = reconstruct(t_recon)

# Plot
plt.figure(figsize=(10,6))
plt.plot(t_cont, x_cont, label="Original Signal")
plt.stem(t_sample, x_sample, linefmt='r-', markerfmt='ro', basefmt='k-', label="Sampled Signal")
plt.plot(t_recon, x_recon, '--', label="Reconstructed Signal")

plt.legend()
plt.grid()
plt.show()