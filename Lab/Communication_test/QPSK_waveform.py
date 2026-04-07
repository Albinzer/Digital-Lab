import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_bits = 20
bit_rate = 1
fc = 5
samples_per_bit = 100

# Generate random bits
bits = np.random.randint(0, 2, num_bits)

# Group bits into pairs
bit_pairs = bits.reshape(-1, 2)

# Mapping (Gray coding)
mapping = {
    (0, 0): (1, 1),
    (0, 1): (-1, 1),
    (1, 1): (-1, -1),
    (1, 0): (1, -1)
}

I = []
Q = []

for pair in bit_pairs:
    i, q = mapping[tuple(pair)]
    I.extend([i] * samples_per_bit)
    Q.extend([q] * samples_per_bit)

I = np.array(I)
Q = np.array(Q)

# Time
t = np.arange(0, len(I)) / samples_per_bit

# Carrier
carrier_I = np.cos(2 * np.pi * fc * t)
carrier_Q = np.sin(2 * np.pi * fc * t)

# QPSK signal
qpsk_signal = I * carrier_I - Q * carrier_Q

# -------- 1. I component --------
plt.figure()
plt.plot(t, I)
plt.title("In-phase Component (I)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


# -------- 2. Q component --------
plt.figure()
plt.plot(t, Q)
plt.title("Quadrature Component (Q)")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


# -------- 3. QPSK Signal --------
plt.figure()
plt.plot(t, qpsk_signal)
plt.title("QPSK Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()