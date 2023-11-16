import numpy as np
import matplotlib.pyplot as plt

#1
N = 100
x = np.random.rand(N)

plt.figure(figsize=(16, 4))
plt.subplot(141)
plt.plot(x)
plt.title('Initial')

for i in range(3):
    x = x * x

    plt.subplot(142 + i)
    plt.plot(x)
    plt.title(f'Iteratia {i + 1}')

plt.tight_layout()
plt.show()
