from skimage import data as sk_image
from matplotlib import pyplot as plt

import smooth_space_filter



if __name__ == '__main__':
    source_image = sk_image.coins()

    median_filter_image = smooth_space_filter.median_filter(source_image, 9)

    plt.subplot(1, 2, 1)
    plt.title("source image")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("median filter image")
    plt.imshow(median_filter_image, cmap="gray")
    plt.show()