import numpy as np
import matplotlib.pyplot as plt

N = 10
n = np.random.randint(0, 2, N)
print("Binary Data:", n)

# Manchester mapping
nnn = []
for bit in n:
    if bit == 1:
        nnn.extend([1, -1])
    else:
        nnn.extend([-1, 1])

nnn = np.array(nnn)

t = np.arange(0, N, 0.01)
y = np.zeros(len(t))

i = 0
l = 0.5

for j in range(len(t)):
    if t[j] <= l:
        y[j] = nnn[i]
    else:
        i += 1
        y[j] = nnn[i]
        l += 0.5

plt.plot(t, y, linewidth=2)
plt.axis([0, N, -1.5, 1.5])
plt.grid()
plt.title("Manchester Coding")
plt.show()
