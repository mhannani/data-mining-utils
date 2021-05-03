from utils.tr_color_2_gr_scale import tr_2_gr_scale
from histogram.calculate_histogram import calculate_histogram
import numpy as np


def compare_img_hist(img_1, img_2):
    """
    Campare two RGB images using histogram.
    :param img_1: array-like image.
    :param img_2: array-liek image.
    :return integer
        difference between histogram
    """

    # We will do that just for gray-scale images to make things easier
    # converting images to gray-scale
    img_1 = tr_2_gr_scale(img_1)
    img_2 = tr_2_gr_scale(img_2)

    # Calculating histograms
    hist_img_1 = calculate_histogram(img_1, [0])
    hist_img_2 = calculate_histogram(img_2, [0])

    return np.sum(np.abs(hist_img_1 - hist_img_2))