import numpy as np
import matplotlib.pyplot as plt
from scipy import datasets
from scipy.fft import dctn, idctn

# 1
Q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
          [12, 12, 14, 19, 26, 28, 60, 55],
          [14, 13, 16, 24, 40, 57, 69, 56],
          [14, 17, 22, 29, 51, 87, 80, 62],
          [18, 22, 37, 56, 68, 109, 103, 77],
          [24, 35, 55, 64, 81, 104, 113, 92],
          [49, 64, 78, 87, 103, 121, 120, 101],
          [72, 92, 95, 98, 112, 100, 103, 99]]


def jpeg_compress(image_array: np.array):
    if image_array.shape[0] % 8 != 0 or image_array.shape[1] % 8 != 0:
        return
    compressed_image = np.zeros(image_array.shape)
    for i in range(0, image_array.shape[0], 8):
        for j in range(0, image_array.shape[1], 8):
            block = image_array[i:i + 8, j:j + 8]
            dct_result = dctn(block)
            compressed_image[i:i + 8, j:j + 8] = Q_jpeg * np.round(dct_result / Q_jpeg)
    return compressed_image


def jpeg_decompress(compressed_image: np.array):
    if compressed_image.shape[0] % 8 != 0 or compressed_image.shape[1] % 8 != 0:
        return
    decompressed_image = np.zeros(compressed_image.shape)
    for i in range(0, compressed_image.shape[0], 8):
        for j in range(0, compressed_image.shape[1], 8):
            compressed_block = compressed_image[i:i + 8, j:j + 8]
            decompressed_image[i:i + 8, j:j + 8] = idctn(compressed_block)
    return decompressed_image


X = datasets.ascent()

plt.subplot(121).imshow(X, cmap=plt.cm.gray)
plt.title('Original')
plt.subplot(122).imshow(jpeg_decompress(jpeg_compress(X)), cmap=plt.cm.gray)
plt.title('JPEG')
plt.show()


# 2

def rgb_to_ycbcr(image: np.array):
    if image.shape[2] != 3:
        return
    ycbcr = np.zeros(image.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            ycbcr[i, j, 0] = 0.299 * image[i, j, 0] + 0.587 * image[i, j, 1] + 0.114 * image[i, j, 2]
            ycbcr[i, j, 1] = 128 - 0.168736 * image[i, j, 0] - 0.331264 * image[i, j, 1] + 0.5 * image[i, j, 2]
            ycbcr[i, j, 2] = 128 + 0.5 * image[i, j, 0] - 0.418688 * image[i, j, 1] - 0.081312 * image[i, j, 2]
    return ycbcr


def ycbcr_to_rgb(image: np.array):
    if image.shape[2] != 3:
        return
    rgb = np.zeros(image.shape)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rgb[i, j, 0] = image[i, j, 0] + 1.402 * (image[i, j, 2] - 128)
            rgb[i, j, 1] = image[i, j, 0] - 0.344136 * (image[i, j, 1] - 128) - 0.714136 * (image[i, j, 2] - 128)
            rgb[i, j, 2] = image[i, j, 0] + 1.772 * (image[i, j, 1] - 128)
    return rgb


def jpeg_compress_ycbcr(rgb_image: np.array):
    if rgb_image.shape[0] % 8 != 0 or rgb_image.shape[1] % 8 != 0:
        return
    ycbcr_image = rgb_to_ycbcr(rgb_image)
    y_jpeg = jpeg_compress(ycbcr_image[:, :, 0])
    cb_jpeg = jpeg_compress(ycbcr_image[:, :, 1])
    cr_jpeg = jpeg_compress(ycbcr_image[:, :, 2])
    ycbcr_jpeg = np.zeros(rgb_image.shape)
    ycbcr_jpeg[:, :, 0] = y_jpeg
    ycbcr_jpeg[:, :, 1] = cb_jpeg
    ycbcr_jpeg[:, :, 2] = cr_jpeg
    return ycbcr_jpeg


X = datasets.face()
X_compressed = jpeg_compress_ycbcr(X)
X_decompressed = np.stack([jpeg_decompress(X_compressed[:, :, x]) for x in range(3)], axis=-1)
X_decompressed = ycbcr_to_rgb(X_decompressed).astype(np.uint8)

plt.subplot(121).imshow(X)
plt.title('Original')
plt.subplot(122).imshow(X_decompressed)
plt.title('JPEG')
plt.show()
