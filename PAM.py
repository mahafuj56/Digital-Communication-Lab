import numpy as np
import matplotlib.pyplot as plt

fc = 20          # Carrier frequency
fm = 2           # Message frequency
fs = 1000        # Sampling frequency
t = 1            # Time duration

n = np.arange(0, t, 1/fs)

duty = 20        # Duty cycle

# =========================
# 2️⃣ Square Wave (Pulse Train)
# =========================
s = np.where(np.mod(n * fc, 1) < duty / 100, 1.0, 0.0)

# Convert negative values to 0 (like MATLAB)
s[s < 0] = 0

# =========================
# 3️⃣ Message Signal
# =========================
m = np.sin(2 * np.pi * fm * (n - 1))

# =========================
# 4️⃣ PAM Signal Generation
# =========================
period_samp = int(len(n) / fc)
ind = np.arange(0, len(n), period_samp)

on_samp = int(np.ceil(period_samp * duty / 100))

pam = np.zeros(len(n))

for i in range(len(ind)):
    end_index = min(ind[i] + on_samp, len(n))
    pam[ind[i]:end_index] = m[ind[i]]

# =========================
# 5️⃣ Plotting (Same Output Style)
# =========================
plt.figure(figsize=(10, 8))

# Square wave
plt.subplot(3,1,1)
plt.plot(n, s)
plt.ylim([-0.2, 1.2])
plt.title("Square Wave (Carrier)")

# Message signal
plt.subplot(3,1,2)
plt.plot(n, m)
plt.ylim([-1.2, 1.2])
plt.title("Message Signal")

# PAM signal
plt.subplot(3,1,3)
plt.plot(n, pam)
plt.ylim([-1.2, 1.2])
plt.title("PAM Signal")

plt.tight_layout()
plt.show()
