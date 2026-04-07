
# Amplitude Shift Keying (ASK) Modulation and Demodulation

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,0,1,0,1,0,1,0,1])           # x=message signal 
bp = 1e-6  # bit-periad

print("Binary Information at transmitter:", x) 

#  Create Of Digital signal
bit = np.repeat(x, 100)                             # bit= 100 sample of digital signal
t1 = np.linspace(0, bp*len(x), len(bit))            # t1= time axis 

plt.figure(figsize=(10,8))

plt.subplot(3,1,1)
plt.plot(t1, bit, linewidth=2.5)
plt.grid(True)
plt.axis([0, bp*len(x), -0.5, 1.5])
plt.ylabel("Amplitude (volt)")
plt.xlabel("Time (sec)")
plt.title("Transmitting Information as Digital Signal")

# ASK Modulation
A1, A2 = 10, 5  # A1=high Amplitude , A2= low Amplitude 
br = 1/bp # bit-rate
f = br*10                       # f= carrier frequency

t2 = np.linspace(0, bp, 100)
m = []

for i in x:
    if i == 1:
        y = A1*np.cos(2*np.pi*f*t2)                             # bit=1 then y= A1*cos(2pift2)
    else:
        y = A2*np.cos(2*np.pi*f*t2)                             # bit=0 then y= A2*cos(2pift2)                          
    m.extend(y)                                                 # m=modulated signal ekotro kore ekta signal make kore 

m = np.array(m)
t3 = np.linspace(0, bp*len(x), len(m))

plt.subplot(3,1,2)
plt.plot(t3, m, linewidth=1)
plt.grid(True)
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (volt)")
plt.title("Waveform for binary ASK Modulation corresponding binary information")

# Demodulation
mn = []
for i in range(len(x)):
    segment = m[i*100:(i+1)*100]
    ref = np.cos(2*np.pi*f*t2)
    z = np.trapz(segment*ref, t2)

    if (2*z/bp) > 7.5:
        mn.append(1)
    else:
        mn.append(0)

print("Binary Information at Receiver:", mn)

# Received signal
bit_rec = np.repeat(mn, 100)
t4 = np.linspace(0, bp*len(mn), len(bit_rec))

plt.subplot(3,1,3)
plt.plot(t4, bit_rec, linewidth=2.5)
plt.grid(True)
plt.axis([0, bp*len(mn), -0.5, 1.5])
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude (volt)")
plt.title("Received information as Digital Signal")

plt.tight_layout()
plt.show()