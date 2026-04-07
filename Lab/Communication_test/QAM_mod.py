import numpy as np
import matplotlib.pyplot as plt

# Number of symbols
N = 200

# Generate random bits
bits = np.random.randint(0, 2, N*4)

# Group into 4 bits
bit_groups = bits.reshape((N, 4))

# Gray coding mapping
mapping = {
    (0,0): -3, # low
    (0,1): -1, # mid
    (1,1):  1, # mid
    (1,0):  3  # high
}

# Generate I and Q
I = np.array([mapping[tuple(b[:2])] for b in bit_groups])
Q = np.array([mapping[tuple(b[2:])] for b in bit_groups])

# QAM Signal
qam_signal = I + 1j*Q

# Time axis
t = np.arange(N)

# ----------- 1. Modulated Signal -------------
plt.figure(figsize=(8,5))
plt.plot(t, np.real(qam_signal), label='In-phase (I)')
plt.plot(t, np.imag(qam_signal), label='Quadrature (Q)')
plt.title("16-QAM Modulated Signal")
plt.xlabel("Symbol Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

# ----------- 2. Constellation Diagram ----------
plt.figure(figsize=(6,6))
plt.scatter(np.real(qam_signal), np.imag(qam_signal))
plt.title("16-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.grid(True)
plt.xticks([-3, -1, 1, 3])
plt.yticks([-3, -1, 1, 3])
plt.axis('equal')
plt.show()