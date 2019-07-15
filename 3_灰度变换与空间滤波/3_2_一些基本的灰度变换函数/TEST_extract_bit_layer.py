import basic_grayscale_transformation
import matplotlib.pyplot as plt
import skimage.data as sk_image

if __name__ == '__main__':

    source_image = sk_image.camera()

    plt.subplot(3, 3, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(3, 3, 2)
    plt.title("1")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 1), cmap="gray")
    plt.subplot(3, 3, 3)
    plt.title("2")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 2), cmap="gray")
    plt.subplot(3, 3, 4)
    plt.title("3")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 3), cmap="gray")
    plt.subplot(3, 3, 5)
    plt.title("4")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 4), cmap="gray")
    plt.subplot(3, 3, 6)
    plt.title("5")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 5), cmap="gray")
    plt.subplot(3, 3, 7)
    plt.title("6")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 6), cmap="gray")
    plt.subplot(3, 3, 8)
    plt.title("7")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 7), cmap="gray")
    plt.subplot(3, 3, 9)
    plt.title("8")
    plt.imshow(basic_grayscale_transformation.extract_bit_layer(source_image, 8), cmap="gray")

    plt.show()