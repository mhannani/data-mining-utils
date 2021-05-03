import numpy as np
from .ndarray_it import ndarray_it


def tr_2_gr_scale(f_img):
    """
    Convert a true-color image given its absolute path to gray-scale image.

    Normally, images are RGB, which means they have 3 channels, one for red,
    one for green and one for blue ...

    To convert an image into gray-scale we leverage each pixel of three
    values(RGB: red-green-blue) using ITU-R BT.601 conversion and each pixel
    will be represented as y = R * 299/1000 + G * 587/1000 + B * 114/1000.
    for more information see :
        *   https://en.wikipedia.org/wiki/YCbCr#ITU-R_BT.601_conversion
        *   https://e2eml.school/convert_rgb_to_grayscale.html

    :param f_img: string
        The path of the image to convert to gray-scale one.
    :return: array_like
        An array of gray-scaled representing the image.
    """

    # ITU-R BT.601 conversion values
    y = [0.299, 0.587, 0.114]

    # convert the path/image into ndarray
    rgb_img = ndarray_it(f_img)

    # leveraging...
    grayed_pixel = np.dot(rgb_img[..., :3], y)

    return grayed_pixel

