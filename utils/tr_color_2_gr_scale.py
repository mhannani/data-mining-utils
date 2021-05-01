from PIL import Image
import numpy as np


def tr_2_gr_scale(f_img):
    """
    Convert a true-color image given its absolute path to gray-scale image.

    :param f_img: string
        The path of the image to convert to gray-scale one.
    :return:
        An array of gray-scaled representing the image.
    """

    # ===> Explanation

    # Normally, images are RGB, which means they have 3 channels, one for red,
    # one for green and one for blue. ... If you have an L mode image,
    # that means it is a single channel image - normally interpreted as greyscale.
    # The L means that is just stores the Luminance.
    # It is very compact, but only stores a greyscale, not colour.

    # convert the image into gray scale using the 'L' option.
    image = Image.open(f_img).convert("L")

    # convert PIL.Image.Image object back to numpy array
    gr_sc_array = np.asarray(image)

    return gr_sc_array

