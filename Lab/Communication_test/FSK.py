# Frequency Shift Keying (FSK) Modulation and Demodulation

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,1,0,1,0,1])
bp = 1e-6

print("Binary Information at Transmitter:", x)

bit = np.repeat(x, 100)
t1 = np.linspace(0, bp*len(x), len(bit))

plt.subplot(3,1,1)
plt.plot(t1, bit)
plt.title("Digital Signal")
plt.grid()

# FSK Modulation
A = 5
br = 1/bp
f1 = br*8
f2 = br*2

t2 = np.linspace(0, bp, 100)
m = []

for i in x:
    if i == 1:
        y = A*np.cos(2*np.pi*f1*t2)
    else:
        y = A*np.cos(2*np.pi*f2*t2)
    m.extend(y)

m = np.array(m)
t3 = np.linspace(0, bp*len(x), len(m))

plt.subplot(3,1,2)
plt.plot(t3, m)
plt.title("FSK Modulated Signal")
plt.grid()

# Demodulation
mn = []
for i in range(len(x)):
    segment = m[i*100:(i+1)*100]
    y1 = np.cos(2*np.pi*f1*t2)
    y2 = np.cos(2*np.pi*f2*t2)

    z1 = np.trapezoid(segment*y1, t2)
    z2 = np.trapezoid(segment*y2, t2)

    if (2*z1/bp) > (A/2):
        mn.append(1)
    else:
        mn.append(0)

print("Binary Information at Receiver:", mn)

bit_rec = np.repeat(mn, 100)
t4 = np.linspace(0, bp*len(mn), len(bit_rec))

plt.subplot(3,1,3)
plt.plot(t4, bit_rec)
plt.title("Received Signal")
plt.grid()

plt.tight_layout()
plt.show()