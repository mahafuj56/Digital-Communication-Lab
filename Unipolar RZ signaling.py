import numpy as np
import matplotlib.pyplot as plt

N = 10
n = np.random.randint(0, 2, N)
print("Binary Data:", n)

t = np.arange(0, N, 0.01)
y = np.zeros(len(t))

i = 0
a = 0
b = 0.5

for j in range(len(t)):
    if a <= t[j] <= b:
        y[j] = n[i]
    elif b < t[j] <= (i + 1):
        y[j] = 0
    else:
        i += 1
        a += 1
        b += 1

plt.plot(t, y, linewidth=2)
plt.xticks (np.arange (0,N+1,1))
plt.axis([0, N, -1.5, 1.5])
plt.grid()
plt.title("Unipolar RZ Signaling")
plt.show()
