
# PAM (Pulse Amplitude Modulation) Signal Generation



import numpy as np
import matplotlib.pyplot as plt

# Parameters
fc = 20
fm = 2
fs = 1000
t = 1

n = np.arange(0, t, 1/fs)

duty = 20  # percent

# 🔥 FIXED: Manual square wave generation
period = int(fs / fc)  # samples per cycle
on_samples = int(period * duty / 100)

s = np.zeros(len(n))

for i in range(0, len(n), period):
    s[i:i+on_samples] = 1   # ON portion

# Message signal
m = np.sin(2*np.pi*fm*n)

# PAM generation
pam = np.zeros(len(n))

for i in range(0, len(n), period):
    pam[i:i+on_samples] = m[i]

# Plot
plt.figure(figsize=(10,7))

plt.subplot(3,1,1)
plt.plot(n, s, linewidth=2)
plt.ylim([-0.2, 1.2])
plt.title("Pulse Train (Square Wave)")
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(n, m, linewidth=2)
plt.ylim([-1.2, 1.2])
plt.title("Message Signal")
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(n, pam, linewidth=2)
plt.ylim([-1.2, 1.2])
plt.title("PAM Signal")
plt.grid(True)

plt.tight_layout()
plt.show()