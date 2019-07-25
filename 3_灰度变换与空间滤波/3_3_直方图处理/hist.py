import numpy as np

def hist_equalization(input_image):
    '''
    直方图均衡（适用于灰度图）
    :param input_image: 原图像
    :return: 均衡后的图像
    '''
    output_imgae = np.copy(input_image) # 输出图像，初始化为输入

    input_image_cp = np.copy(input_image) # 输入图像的副本

    m, n = input_image_cp.shape # 输入图像的尺寸（行、列）

    pixels_total_num = m * n # 输入图像的像素点总数

    input_image_grayscale_P = [] # 输入图像中各灰度级出现的概率，亦即输入图像直方图

    # 求输入图像中各灰度级出现的概率，亦即输入图像直方图
    for i in range(256):
        input_image_grayscale_P.append(np.sum(input_image_cp == i) / pixels_total_num)

    # 求解输出图像
    t = 0               # 输入图像的灰度级分布函数F
    for i in range(256):

        t = t + input_image_grayscale_P[i]

        output_imgae[np.where(input_image_cp == i)] = 255 * t

    return output_imgae