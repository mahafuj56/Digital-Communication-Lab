import numpy as np
import matplotlib.pyplot as plt

# Input signal
t = np.linspace(0, 1, 200)
x = np.sin(2 * np.pi * 5 * t)

# DPCM
step = 0.2
pred = np.zeros(len(x))
error = np.zeros(len(x))
q_error = np.zeros(len(x))
recon = np.zeros(len(x))

for i in range(1, len(x)):
    pred[i] = x[i-1]
    error[i] = x[i] - pred[i]
    q_error[i] = step * np.round(error[i] / step)
    recon[i] = recon[i-1] + q_error[i]

# Plot
plt.figure(figsize=(10,8))

plt.subplot(4,1,1)
plt.plot(t, x)
plt.title("Original Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,2)
plt.plot(t, error)
plt.title("Prediction Error Signal")
plt.xlabel("Time")
plt.ylabel("Error")
plt.grid()

plt.subplot(4,1,3)
plt.plot(t, q_error)
plt.title("Quantized Error Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,4)
plt.plot(t, recon)
plt.title("Reconstructed Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
