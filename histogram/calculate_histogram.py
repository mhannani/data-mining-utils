import numpy as np


def calculate_histogram(img, channel):
    """
    Calculates the histogram of a given image.
    :param img: an image to which to calculate the histogram.
    :param channel: a 1-element list
    :return tuple of array
        (hist_gs_or_red, hist_green, hist_blue) indicating the histogram along each color channel
    """

    # histogram arrays for each channel
    hist_gs_or_red = np.zeros((256, 1), dtype=np.int32)
    hist_green = np.zeros((256, 1), dtype=np.int32)
    hist_blue = np.zeros((256, 1), dtype=np.int32)

    # Calculate the histogram for red channel for RGB images
    # or the the first channel for gray-scale images.
    if channel == [0]:
        # one-dimensional array
        if img.ndim == 1:
            raise Exception('Cannot calculate the hist of one-dimensional array.')

        # if there is one channel, or in case of gray-scale images, it's OK!
        elif img.ndim == 2:
            for pixel in np.ceil(img.flatten()).astype(np.int):
                hist_gs_or_red[pixel] = hist_gs_or_red[pixel] + 1

        # an RGB image
        elif img.ndim == 3:
            for pixel in np.ceil(img[:, :, 0:1].flatten()).astype(np.int):
                hist_gs_or_red[pixel] = hist_gs_or_red[pixel] + 1

        # more than 3 dimensions
        else:
            raise Exception('Cannot calculate the hist of more than 3-dimensional array.')

        return hist_gs_or_red

    # Calculate the histogram of green channel for RGB images
    elif channel == [1]:
        # Not 3-D array that represent the image with 3 color channels.
        if img.ndim <= 2:
            raise Exception('Cannot calculate the hist of green channel for non-rgb images/ 3-D array')

        # If it's a 3-D array of 3 color channels
        elif img.ndim == 3:
            for pixel in np.ceil(img[:, :, 1:2].flatten()).astype(np.int):
                hist_green[pixel] = hist_green[pixel] + 1

        # more than 3 dimensions
        else:
            raise Exception('Cannot calculate the hist of more than 3-dimensional array.')
        return hist_green

    # Calculate the histogram of green channel for RGB images
    elif channel == [2]:
        if img.ndim <= 2:
            raise Exception('Cannot calculate the hist of blue channel for non-rgb images/ 3-D array')
        elif img.ndim == 3:
            for pixel in np.ceil(img[:, :, 2:].flatten()).astype(np.int):
                hist_blue[pixel] = hist_blue[pixel] + 1
        return hist_blue

    # Invalid value of channel parameter
    else:
        raise Exception('ValueError: only [0], [1], [2] are possible as value for the channel parameter.')
