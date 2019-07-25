from skimage import data as sk_image
from matplotlib import pyplot as plt

import smooth_space_filter

if __name__ == '__main__':

    source_image = sk_image.coins()

    means_filter_image = smooth_space_filter.means_filter(source_image, 9)

    plt.subplot(1, 2, 1)
    plt.title("source image")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("means filter image")
    plt.imshow(means_filter_image, cmap="gray")
    plt.show()