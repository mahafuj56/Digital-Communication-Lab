# PSK Modulation and Demodulation

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,0,1,0,1,0,1,0,1])
bp, s = 1e-6, 100
bit = np.repeat(x, s)
t = np.linspace(0, bp, s)
f = 2 / bp
A = 5

m = np.concatenate([A*np.cos(2*np.pi*f*t + (0 if b else np.pi)) for b in x])
carrier = np.cos(2*np.pi*f*t)

mn = [1 if (2*np.trapz(m[i:i+s]*carrier, t)/bp) > 0 else 0
      for i in range(0, len(m), s)]

plt.figure(figsize=(10,8))

plt.subplot(311)
plt.plot(np.linspace(0, bp*len(x), len(bit)), bit, lw=2)
plt.axis([0, bp*len(x), -0.5, 1.5])
plt.grid()
plt.title("PSK Input Signal")

plt.subplot(312)
plt.plot(np.linspace(0, bp*len(x), len(m)), m)
plt.grid()
plt.title("PSK Modulated Signal")

plt.subplot(313)
plt.plot(np.linspace(0, bp*len(mn), len(np.repeat(mn,s))), np.repeat(mn,s), lw=2)
plt.axis([0, bp*len(mn), -0.5, 1.5])
plt.grid()
plt.title("PSK Demodulated Signal")

print("Receiver Bits:", mn)
plt.tight_layout()
plt.show()
