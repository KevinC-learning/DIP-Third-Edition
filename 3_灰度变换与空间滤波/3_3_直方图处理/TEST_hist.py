import hist
import matplotlib.pyplot as plt
import skimage.data as sk_image
import numpy as np

if __name__ == '__main__':

    source_image = sk_image.coins()

    image_hist = hist.hist_equalization(source_image)

    # 图
    plt.subplot(2, 2, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(2, 2, 2)
    plt.title("after")
    plt.imshow(image_hist, cmap="gray")
    # 直方图
    plt.subplot(2, 2, 3)
    plt.title("hist before")
    plt.hist(np.array(source_image).flatten(), bins=256)
    plt.subplot(2, 2, 4)
    plt.title("hist after")
    plt.hist(np.array(image_hist).flatten(), bins=256)

    plt.show()