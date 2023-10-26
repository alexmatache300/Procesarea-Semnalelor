import numpy as np
import matplotlib.pyplot as plt

#1
N = 8

matrice_fourier = np.zeros((N, N), dtype=np.complex64)

for k in range(N):
    for n in range(N):
        matrice_fourier[k, n] = np.exp(-2j * np.pi * k * n / N) / np.sqrt(N)

fig, axs = plt.subplots(N,figsize=(10, 10))

for i in range(N):
    axs[i].plot(np.real(matrice_fourier[i, :]), np.imag(matrice_fourier[i, :]))

plt.tight_layout()
plt.show()
