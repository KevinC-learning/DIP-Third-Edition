from matplotlib import pyplot as plt

import skimage as sk
import sharpen_space_filter

if __name__ == '__main__':

    source_image = sk.data.camera()

    unsharpened_masking_image = sharpen_space_filter.unsharpened_masking(source_image, 2)

    plt.subplot(1, 2, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("after")
    plt.imshow(unsharpened_masking_image, cmap="gray")
    plt.show()