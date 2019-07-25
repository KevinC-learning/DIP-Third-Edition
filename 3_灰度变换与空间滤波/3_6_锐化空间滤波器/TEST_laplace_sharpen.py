from matplotlib import pyplot as plt

import skimage as sk
import sharpen_space_filter

if __name__ == '__main__':

    source_image = sk.data.camera()

    laplace_sharpen_image = sharpen_space_filter.laplace_sharpen(source_image, -0.5)

    plt.subplot(1, 2, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("after")
    plt.imshow(laplace_sharpen_image, cmap="gray")
    plt.show()