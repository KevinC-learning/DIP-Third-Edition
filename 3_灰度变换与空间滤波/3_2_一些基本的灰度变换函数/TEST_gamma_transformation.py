import basic_grayscale_transformation
import matplotlib.pyplot as plt
import skimage.data as sk_image

if __name__ == '__main__':
    source_image = sk_image.camera()

    image_r_0_dot_5 = basic_grayscale_transformation.gamma_transformation(source_image, 1, 0.5)
    image_r_1_dot_5 = basic_grayscale_transformation.gamma_transformation(source_image, 1, 2)
    image_r_1 = basic_grayscale_transformation.gamma_transformation(source_image, 1, 1)

    plt.subplot(2, 2, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(2, 2, 2)
    plt.title("after when r = 0.5")
    plt.imshow(image_r_0_dot_5, cmap="gray")
    plt.subplot(2, 2, 3)
    plt.title("after when r = 2")
    plt.imshow(image_r_1_dot_5, cmap="gray")
    plt.subplot(2, 2, 4)
    plt.title("after when r = 1")
    plt.imshow(image_r_1, cmap="gray")
    plt.show()