import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N = 1000

time = np.arange(N)

trend = 0.002 * time**2

season = 100 * np.sin(2 * np.pi * 0.05 * time) + 50 * np.sin(2 * np.pi * 0.2 * time)

noise = np.random.normal(0, 1, N)

time_series = trend + season + noise

plt.figure(figsize=(12, 6))

plt.subplot(4, 1, 1)
plt.plot(time, time_series, label='Seria de Timp')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(time, trend, label='Trend')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(time, season, label='Sezon')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(time, noise, label='Zgomot')
plt.legend()

plt.tight_layout()
plt.show()

