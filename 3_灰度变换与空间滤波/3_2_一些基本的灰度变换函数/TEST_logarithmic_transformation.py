import basic_grayscale_transformation
import matplotlib.pyplot as plt
import skimage.data as sk_image

if __name__ == '__main__':

    source_image = sk_image.camera()
    image_after_logarithmic_transformation = basic_grayscale_transformation.logarithmic_transformation(source_image, 1)

    plt.subplot(1, 2, 1)
    plt.title("before")
    plt.imshow(source_image, cmap="gray")
    plt.subplot(1, 2, 2)
    plt.title("after")
    plt.imshow(image_after_logarithmic_transformation, cmap="gray")
    plt.show()
