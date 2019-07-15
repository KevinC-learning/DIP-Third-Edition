import basic_grayscale_transformation
import matplotlib.pyplot as plt
import skimage.data as sk_image

if __name__ == '__main__':

    source_image = sk_image.camera()
    reverse_image = basic_grayscale_transformation.image_reverse(source_image)

    plt.subplot(1, 2, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("after")
    plt.imshow(reverse_image, cmap="gray")
    plt.show()