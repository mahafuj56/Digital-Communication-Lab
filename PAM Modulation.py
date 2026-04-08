import numpy as np
import matplotlib.pyplot as plt

# Parameters
n, spb, A = 20, 100, 5

# Generate bits and PAM signal
bits = np.random.randint(0, 2, n)
pam = np.repeat(np.where(bits, A, -A), spb)

t = np.arange(len(pam)) / spb

# Add noise
received = pam + np.random.normal(0, 1, len(pam))

# Demodulation
points = np.arange(spb//2, len(received), spb)
samples = received[points]
recovered = (samples > 0).astype(int)

demod = np.repeat(np.where(recovered, A, -A), spb)

# Plot
plt.figure(figsize=(10,10))

plt.subplot(4,1,1)
plt.step(range(n), bits, where='post')
plt.title("Original Binary Signal")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid()

plt.subplot(4,1,2)
plt.plot(t, pam)
plt.title("PAM Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,3)
plt.plot(t, received)
plt.scatter(points/spb, samples, color='red')
plt.title("Received Signal with Noise")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,4)
plt.plot(t, demod)
plt.title("Demodulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
