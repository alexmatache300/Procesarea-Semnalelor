import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import cholesky


# 1
def sample_from_2D_gaussian(mean, covariance_matrix, num_samples):
    dim = len(mean)
    l = cholesky(covariance_matrix)
    z = np.random.normal(size=(num_samples, dim))
    return mean + np.dot(z, l.T)


mean_1D = 0
variance_1D = 1
samples_1D = np.random.normal(mean_1D, np.sqrt(variance_1D), 1000)

plt.hist(samples_1D, bins=30, density=True, alpha=0.5, color='b')
plt.title('Distributie Gaussiana Unidimensionala')
plt.xlabel('Valoare')
plt.ylabel('Frecventa')
plt.show()

mean_2D = np.array([1, 2])
covariance_matrix_2D = np.array([[2, 1], [1, 2]])
samples_2D = sample_from_2D_gaussian(mean_2D, covariance_matrix_2D, 1000)

plt.scatter(samples_2D[:, 0], samples_2D[:, 1], alpha=0.5, color='r')
plt.title('Distributie Gaussiana Bidimensionala')
plt.xlabel('Valoare X')
plt.ylabel('Valoare Y')
plt.show()
