import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from itertools import product

# a
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

# b
autocorrelation = np.correlate(time_series, time_series, mode='full')

autocorrelation /= np.max(autocorrelation)

plt.figure(figsize=(12, 4))
plt.plot(np.arange(-N + 1, N), autocorrelation, label='Autocorelație')
plt.xlabel('Lag')
plt.ylabel('Autocorelație')
plt.legend()
plt.show()

# c
p = 10
model = sm.tsa.AutoReg(time_series, lags=p, trend='n')
result = model.fit()

predictions = result.predict(start=p, end=N - 1)

plt.figure(figsize=(12, 6))
plt.plot(time, time_series, label='Seria de Timp Originala')
plt.plot(time[p:], predictions, label=f'Predictii AR(p={p})', color='red')
plt.legend()
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.title('Seria de Timp Originala si Predictiile AR')
plt.show()

# d
param_grid = {'p': range(1, 11), 'm': range(1, 11)}

best_params = {'p': None, 'm': None}
best_mse = float('inf')

for params in product(param_grid['p'], param_grid['m']):
    p, m = params
    model = sm.tsa.AutoReg(time_series, lags=p, trend='n')
    result = model.fit()

    predictions = result.predict(start=p, end=N - 1)

    mse = mean_squared_error(time_series[p:], predictions)

    if mse < best_mse:
        best_mse = mse
        best_params['p'] = p
        best_params['m'] = m

print(f'Cea mai buna combinatie de parametri: {best_params}')
print(f'MSE pentru cea mai buna combinatie: {best_mse}')
