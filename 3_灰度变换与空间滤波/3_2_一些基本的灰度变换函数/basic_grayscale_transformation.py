import numpy as np

def image_reverse(input_image):
    '''
    图像反转
    :param input_image: 原图像
    :return: 反转后的图像
    '''
    input_image_cp = np.copy(input_image) # 输入图像的副本

    pixels_value_max = np.max(input_image_cp) # 输入图像像素的最大值

    output_imgae = pixels_value_max - input_image_cp # 输出图像

    return output_imgae


def logarithmic_transformation(input_image, c):
    '''
    对数变换
    :param input_image: 原图像
    :param c: 对数变换超参数
    :return: 对数变换后的图像
    '''
    input_image_cp = np.copy(input_image) # 输入图像的副本

    output_imgae = c * np.log(1 + input_image_cp.astype(int)) # 输出图像

    return output_imgae


def gamma_transformation(input_image, c, gamma):
    '''
    伽马变换
    :param input_image: 原图像
    :param c: 伽马变换超参数
    :param gamma: 伽马值
    :return: 伽马变换后的图像
    '''
    input_image_cp = np.copy(input_image)  # 输入图像的副本

    output_imgae = c * np.power(input_image_cp.astype(int), gamma) # 输出图像

    return output_imgae


def contrast_stretch(input_image):
    '''
    对比图拉伸（此实现为阈值处理，阈值为均值）
    :param input_image: 输入图像
    :return: 对比图拉伸后的图像
    '''
    input_image_cp = np.copy(input_image) # 输入图像的副本

    pixels_value_mean = np.mean(input_image_cp) # 输入图像的平均灰度值

    # 对比图拉伸（注：该实现顺序不能颠倒）
    input_image_cp[np.where(input_image_cp <= pixels_value_mean)] = 0
    input_image_cp[np.where(input_image_cp > pixels_value_mean)] = 1

    output_image = input_image_cp

    return output_image


def grayscale_layer(input_image, spotlight_range_min, spotlight_range_max, means):
    '''
    灰度级分层
    :param input_image: 原图像
    :param spotlight_range_min: 所突出的灰度级范围最小值
    :param spotlight_range_max: 所突出的灰度级范围最大值
    :param means: 分层方式（1，2）
    :return: 灰度级分层后的图像
    '''
    input_image_cp = np.copy(input_image) # 输入图像的副本

    if means == 1: # 方式一（突出指定范围内255，并且变暗非范围内0）
        input_image_cp = np.where((input_image_cp >= spotlight_range_min) & (input_image_cp <= spotlight_range_max), 255, 0)
    elif means == 2: # 方式二（仅突出指定范围内255）
        input_image_cp[np.where((input_image_cp >= spotlight_range_min) & (input_image_cp <= spotlight_range_max))] = 255
    else:
        print("please enter the number of means from 1 to 2")
        return

    output_image = input_image_cp

    return output_image


def extract_bit_layer(input_image, layer_num):
    '''
    提取比特层
    :param input_image: 原图像
    :param layer_num: 提取层
    :return: 提取到的比特层
    '''
    input_image_cp = np.copy(input_image)  # 输入图片的副本

    if layer_num == 1:
        input_image_cp = np.where((input_image_cp >= 0) & (input_image_cp < 2), 255, 0)
    elif layer_num == 2:
        input_image_cp = np.where((input_image_cp >= 2) & (input_image_cp < 4), 255, 0)
    elif layer_num == 3:
        input_image_cp = np.where((input_image_cp >= 4) & (input_image_cp < 8), 255, 0)
    elif layer_num == 4:
        input_image_cp = np.where((input_image_cp >= 8) & (input_image_cp < 16), 255, 0)
    elif layer_num == 5:
        input_image_cp = np.where((input_image_cp >= 16) & (input_image_cp < 32), 255, 0)
    elif layer_num == 6:
        input_image_cp = np.where((input_image_cp >= 32) & (input_image_cp < 64), 255, 0)
    elif layer_num == 7:
        input_image_cp = np.where((input_image_cp >= 64) & (input_image_cp < 128), 255, 0)
    elif layer_num == 8:
        input_image_cp = np.where((input_image_cp >= 128) & (input_image_cp < 256), 255, 0)
    else:
        print("please enter the number of bit layers from 1 to 8")

    output_image = input_image_cp

    return output_image