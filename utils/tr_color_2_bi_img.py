def tr_color_2_bi_img(img, threshold):
    """
    Convert an image into binary representation.

    To convert an image from rgb representation to binary image, we've first to convert it into gray-scale
    by leveraging each pixel of three values(RGB: red-green-blue) using ITU-R BT.601 conversion and each pixel
    will be represented as y = R * 299/1000 + G * 587/1000 + B * 114/1000.
    the first step is done by using the implemented function `tr_color_2_bi_img`, the remaining step
    is to leverage the value of each pixel to either 0 or 1 to represent the image as gray-scale.

    :param img: an array-like
        an array representing the image in RGB color map.
    :param threshold: integer
        An integer to use as threshold for to shift
        value greater than it ot 1(white)
        and 0(black) otherwise.
    :return: an array-like with 0 and 1 values as a binary representation of the image.
    """







