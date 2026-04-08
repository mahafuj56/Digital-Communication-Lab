import numpy as np
import matplotlib.pyplot as plt

# Random bits
N = 200
bits = np.random.randint(0, 2, N * 4).reshape(N, 4)

# 16-QAM Gray mapping
m = {(0,0):-3, (0,1):-1, (1,1):1, (1,0):3}

I = np.array([m[tuple(b[:2])] for b in bits])
Q = np.array([m[tuple(b[2:])] for b in bits])

qam = I + 1j * Q
t = np.arange(N)

# 1. Modulated Signal
plt.figure(figsize=(8,5))
plt.plot(t, qam.real, label='In-phase (I)')
plt.plot(t, qam.imag, label='Quadrature (Q)')
plt.title("16-QAM Modulated Signal")
plt.xlabel("Symbol Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()

# 2. Constellation Diagram
plt.figure(figsize=(6,6))
plt.scatter(qam.real, qam.imag)
plt.title("16-QAM Constellation Diagram")
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.xticks([-3, -1, 1, 3])
plt.yticks([-3, -1, 1, 3])
plt.grid()
plt.axis('equal')
plt.show()
