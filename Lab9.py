import numpy as np
import matplotlib.pyplot as plt

# 1
np.random.seed(42)
N = 1000
time = np.arange(N)
trend = 0.002 * time ** 2
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

#2

alpha = 0.1

exp_smoothed_series = np.zeros_like(time_series)

exp_smoothed_series[0] = time_series[0]
for t in range(1, N):
    exp_smoothed_series[t] = alpha * time_series[t] + (1 - alpha) * exp_smoothed_series[t - 1]

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(time, time_series, label='Seria de Timp')
plt.plot(time, exp_smoothed_series, label='Mediere Exponențiala')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, time_series - exp_smoothed_series, label='Diferenta (Seria de Timp - Mediere Exponentiala)')
plt.legend()

plt.tight_layout()
plt.show()

# 3
mu = np.mean(time_series)
theta = 0.8

epsilon = np.random.normal(0, 1, N)

ma_series = np.zeros_like(time_series)

ma_series[0] = mu + epsilon[0]
for t in range(1, N):
    ma_series[t] = mu + epsilon[t] + theta * epsilon[t - 1]

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(time, time_series, label='Seria de Timp')
plt.plot(time, ma_series, label='Model MA(1)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time, time_series - ma_series, label='Diferenta (Seria de Timp - Model MA(1))')
plt.legend()

plt.tight_layout()
plt.show()
