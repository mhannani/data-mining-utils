import numpy as np
from .ndarray_it import ndarray_it
from .tr_color_2_gr_scale import tr_2_gr_scale


def tr_color_2_bi_img(f_img, threshold):
    """
    Convert an image into binary representation.

    To convert an image from rgb representation to binary image, we've first to convert it into gray-scale
    by leveraging each pixel of three values(RGB: red-green-blue) using ITU-R BT.601 conversion and each pixel
    will be represented as y = R * 299/1000 + G * 587/1000 + B * 114/1000.
    the first step is done by using the implemented function `tr_color_2_bi_img`, the remaining step
    is to leverage the value of each pixel to either 0 or 1 to represent the image as gray-scale.

    :param f_img: an array-like
        The path, python lit or np.ndarray of the image to convert to gray-scale one.
    :param threshold: integer
        An integer to use as threshold for to shift value greater than it ot 1(white)
        and 0(black) otherwise.
    :return: an array-like with 0 and 1 values as a binary representation of the image.
    """

    # convert the path/image into ndarray
    rgb_img = ndarray_it(f_img)

    # convert the image to gray scale
    gray_scaled_img = tr_2_gr_scale(rgb_img)

    # get the image's information
    height, width, channels = rgb_img.shape

    # binary array
    binary_img = np.zeros((height, width))

    # threshold each pixel
    for i in np.arange(height):
        for j in np.arange(width):
            current_pixel = gray_scaled_img.item(i, j)
            if current_pixel > threshold:
                binary_img.itemset((i, j), 1)

    return binary_img














