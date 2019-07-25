import numpy as np
import sys
import scipy.signal

sys.path.insert(0, '../3_5_平滑空间滤波器')
import smooth_space_filter

def laplace_sharpen(input_image, c):
    '''
    拉普拉斯锐化
    :param input_image: 输入图像
    :param c: 锐化系数
    :return: 输出图像
    '''
    input_image_cp = np.copy(input_image)  # 输入图像的副本

    # 拉普拉斯滤波器
    laplace_filter = np.array([
        [1, 1, 1],
        [1, -8, 1],
        [1, 1, 1],
    ])

    input_image_cp = np.pad(input_image_cp, (1, 1), mode='constant', constant_values=0)  # 填充输入图像

    m, n = input_image_cp.shape  # 填充后的输入图像的尺寸

    output_image = np.copy(input_image_cp)  # 输出图像

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            R = np.sum(laplace_filter * input_image_cp[i - 1:i + 2, j - 1:j + 2])  # 拉普拉斯滤波器响应

            output_image[i, j] = input_image_cp[i, j] + c * R

    output_image = output_image[1:m - 1, 1:n - 1]  # 裁剪

    return output_image


def unsharpened_masking(input_image, k):
    '''
    非锐化屏蔽
    :param input_image: 输入图像
    :param k: 权重参数
    :return: 输出图像
    '''
    input_image_cp = np.copy(input_image)  # 输入图像的副本

    # 均值滤波器模糊处理
    blur_input_image = smooth_space_filter.means_filter(input_image_cp, 3)

    output_image = input_image_cp + k * (input_image_cp - blur_input_image)  # 非锐化屏蔽/高提升滤波

    return output_image


def sharpen_gradient(input_image):
    '''
    梯度锐化
    :param input_image: 输入图像
    :return: 输出图像
    '''
    input_image_cp = np.copy(input_image)  # 输入图像的副本

    # sobel算子
    sobel_kernel_1 = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ])
    sobel_kernel_2 = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ])

    output_image = np.abs(scipy.signal.convolve2d(input_image_cp, sobel_kernel_1, mode='same')) + np.abs(scipy.signal.convolve2d(input_image_cp, sobel_kernel_2, mode='same'))

    return output_image