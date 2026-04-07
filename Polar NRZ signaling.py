import numpy as np
import matplotlib.pyplot as plt

N = 10
n = np.random.randint(0, 2, N)
print("Binary Data:", n)

# Mapping
nn = np.where(n == 1, 1, -1)

t = np.arange(0, N, 0.01)
y = np.zeros(len(t))

i = 0
for j in range(len(t)):
    if t[j] < (i + 1):
        y[j] = nn[i]
    else:
        i += 1
        y[j] = nn[i]

plt.plot(t, y, linewidth=2)
plt.axis([0, N, -1.5, 1.5])
plt.xticks (np.arange(0,N+1,1))
plt.grid()
plt.title("Polar NRZ Signaling")
plt.show()
