# Unipolar NRZ (Non-Return to Zero) Signal Generation



import numpy as np
import matplotlib.pyplot as plt

N = 10
n = np.array([0,1,1,0,0,0,1,0,1,0])

t = np.arange(0, N, 0.01)

y = []
i = 0
for time in t:
    if time >= i+1:
        i += 1
    y.append(n[i])

plt.plot(t, y, linewidth=2)
plt.axis([0, N, -1.5, 1.5])
plt.grid(True)
plt.title("Unipolar NRZ Signaling")
plt.show()