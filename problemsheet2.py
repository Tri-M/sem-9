import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve

def generate_ring_image(size):
    image = np.zeros((size, size), dtype=int)
    for i in range(size):
        for j in range(size):
            image[i, j] = min(i, j, size - i - 1, size - j - 1)
    return image

image = generate_ring_image(16)

plt.figure(figsize=(8, 8))
plt.title("16x16 Ring Image")
plt.imshow(image, cmap='gray')
plt.show()

