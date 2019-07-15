import basic_grayscale_transformation
import matplotlib.pyplot as plt
import skimage.data as sk_image

if __name__ == '__main__':

    source_image = sk_image.camera()

    image_grayscale_layer_1 = basic_grayscale_transformation.grayscale_layer(source_image, 0, 50, 1)
    image_grayscale_layer_2 = basic_grayscale_transformation.grayscale_layer(source_image, 0, 50, 2)

    plt.subplot(1, 3, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 3, 2)
    plt.title("after 1")
    plt.imshow(image_grayscale_layer_1, cmap="gray")
    plt.subplot(1, 3, 3)
    plt.title("after 2")
    plt.imshow(image_grayscale_layer_2, cmap="gray")

    plt.show()