import numpy as np
import matplotlib.pyplot as plt

# Continuous signal parameters
f = 2
t = np.linspace(0, 1, 1000)

# Original signal
x = np.sin(2 * np.pi * f * t)

# Sampling
fs = 20
ts = np.arange(0, 1, 1/fs)
xs = np.sin(2 * np.pi * f * ts)

# Reconstruction
t_rec = np.linspace(0, 1, 1000)
x_rec = np.interp(t_rec, ts, xs)

# -------- 1. Continuous Signal --------
plt.figure()
plt.plot(t, x)
plt.title("Continuous Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# -------- 2. Sampled Signal --------
plt.figure()
plt.stem(ts, xs)
plt.title("Sampled Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# -------- 3. Reconstructed Signal --------
plt.figure()
plt.plot(t_rec, x_rec, label='Reconstructed')
plt.plot(t, x, '--', label='Original')
plt.title("Reconstructed Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
