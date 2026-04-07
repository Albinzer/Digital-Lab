import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.randint(0, 2, 100)

# Group into pairs
data_pairs = data.reshape(-1, 2)                                # array.reshape(rows, columns) 
                                                                #-1 means:
                                                                # "NumPy will automatically calculate the number of rows"

# QPSK mapping
mapping = {
    (0,0): (1+1j),
    (0,1): (-1+1j),
    (1,1): (-1-1j),
    (1,0): (1-1j)
}

# Modulation (symbols)
symbols = np.array([mapping[tuple(b)] for b in data_pairs])                                     

# ================= PERFECT QPSK SIGNAL =================
fc = 5
samples_per_symbol = 50

t_symbol = np.arange(samples_per_symbol) / samples_per_symbol                                   #np.arange(start, stop, step)

signal = []

for s in symbols:                                                                               # Symbol → Waveform (cos + sin) → Full Signal
    I = s.real
    Q = s.imag                                                                                   # QPSK Equation : Signal = I·cos(2πf t) + Q·sin(2πf t)
    segment = I * np.cos(2 * np.pi * fc * t_symbol) + Q * np.sin(2 * np.pi * fc * t_symbol)
    signal.extend(segment)

signal = np.array(signal)
time_axis = np.linspace(0, 1, len(signal))

# ================= DEMODULATION =================                                               # Received Symbol → Check Position → Recover Bits= demodulation
demod_bits = []
for s in symbols:
    if s.real > 0 and s.imag > 0:
        demod_bits.extend([0,0])
    elif s.real < 0 and s.imag > 0:
        demod_bits.extend([0,1])
    elif s.real < 0 and s.imag < 0:
        demod_bits.extend([1,1])
    else:
        demod_bits.extend([1,0])
demod_bits = np.array(demod_bits)

# ================= PLOTS (NO SUBPLOT) =================

# 1. QPSK Modulated Signal
plt.figure(figsize=(6,4))
plt.plot(time_axis[:500], signal[:500])
plt.title("QPSK Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()


# 2. QPSK Demodulated Signal
plt.figure(figsize=(6,4))
plt.stem(demod_bits[:20])
plt.title("QPSK Demodulated Signal")
plt.xlabel("Index")
plt.ylabel("Bit")
plt.ylim(-0.2, 1.2)
plt.grid()


# 3. QPSK Constellation Diagram
plt.figure(figsize=(5,5))
plt.scatter(symbols.real, symbols.imag)
plt.title("QPSK Constellation Diagram")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid()
plt.show()

# ================= OUTPUT =================
print("Original:", data[:20])
print("Demodulated:", demod_bits[:20])