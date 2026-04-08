import numpy as np
import matplotlib.pyplot as plt

# Random bits and QPSK mapping
data = np.random.randint(0, 2, 100)
pairs = data.reshape(-1, 2)

mapping = {
    (0,0): 1+1j,
    (0,1): -1+1j,
    (1,1): -1-1j,
    (1,0): 1-1j
}

symbols = np.array([mapping[tuple(p)] for p in pairs])

# QPSK signal generation
fc, sps = 5, 50
t = np.arange(sps) / sps

signal = np.concatenate([
    s.real * np.cos(2*np.pi*fc*t) + s.imag * np.sin(2*np.pi*fc*t)
    for s in symbols
])

time = np.linspace(0, 1, len(signal))

# Demodulation
demod_bits = np.array([
    bit
    for s in symbols
    for bit in (
        [0,0] if s.real > 0 and s.imag > 0 else
        [0,1] if s.real < 0 and s.imag > 0 else
        [1,1] if s.real < 0 and s.imag < 0 else
        [1,0]
    )
])

# 1. Modulated Signal
plt.figure(figsize=(6,4))
plt.plot(time[:500], signal[:500])
plt.title("QPSK Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# 2. Demodulated Bits
plt.figure(figsize=(6,4))
plt.stem(demod_bits[:20])
plt.title("QPSK Demodulated Signal")
plt.xlabel("Index")
plt.ylabel("Bit")
plt.ylim(-0.2, 1.2)
plt.grid()
plt.show()

# 3. Constellation Diagram
plt.figure(figsize=(5,5))
plt.scatter(symbols.real, symbols.imag)
plt.title("QPSK Constellation Diagram")
plt.xlabel("In-phase")
plt.ylabel("Quadrature")
plt.grid()
plt.show()

print("Original:", data[:20])
print("Demodulated:", demod_bits[:20])
