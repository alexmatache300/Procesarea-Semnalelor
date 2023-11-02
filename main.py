import numpy as np
import matplotlib.pyplot as plt
import time

# 1

dimensions = [128, 256, 512, 1024, 2048, 4096, 8192]

execution_times_own = []
execution_times_np_fft = []

for N in dimensions:
    x = np.random.rand(N)

    start_time = time.time()


    def dft_own(x):
        N = len(x)
        n = np.arange(N)
        k = n.reshape((N, 1))
        M = np.exp(-2j * np.pi * k * n / N)
        return np.dot(M, x)


    result_dft_own = dft_own(x)
    end_time = time.time()
    execution_time_own = end_time - start_time
    execution_times_own.append(execution_time_own)

    start_time = time.time()
    result_np_fft = np.fft.fft(x)
    end_time = time.time()
    execution_time_np_fft = end_time - start_time
    execution_times_np_fft.append(execution_time_np_fft)

plt.figure(figsize=(10, 6))
plt.plot(dimensions, execution_times_own, label='Implementarea Proprie (DFT)')
plt.plot(dimensions, execution_times_np_fft, label='numpy.fft')
plt.yscale('log')
plt.xlabel('Dimensiunea Vectorului N')
plt.ylabel('Timp (secunde)')
plt.title('Compararea Timpilor de Execuție pentru DFT și numpy.fft')
plt.legend()
plt.grid()
plt.show()
