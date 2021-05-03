from histogram.calculate_histogram import calculate_histogram
import matplotlib.pyplot as plt
import numpy as np


def plot_histograms_together(img):
    """
    plot three histogram at the same figure of the three color channel.
    :param img: an image or path of image.
    :return None.
    """
    colors = ['red', 'green', 'blue']
    channel = ' channel'
    color_channel = [color + channel for color in colors]

    if isinstance(img, str) or isinstance(img, np.ndarray):
        # Create a figure
        fig = plt.figure(figsize=(15, 10))

        # img as string (path or image).
        if isinstance(img, str):
            img = plt.imread(img)

        # rgb image as ndarray
        if img.ndim == 3 and img.shape[2] == 3:
            # Compute the histogram of first color channel (red color channel)
            hist_gs_red = calculate_histogram(img, [0])
            hist_green = calculate_histogram(img, [1])
            hist_blue = calculate_histogram(img, [2])

            # add grid of figures
            ax = fig.add_subplot(2, 2, 1)

            # show different hists at the same first grid figure
            plt.plot(hist_gs_red, color='r')
            plt.plot(hist_green, color='g')
            plt.plot(hist_blue, color='b')
            plt.title('All color channels')

            # iterate over histogram for different color channel
            for i, color in enumerate(colors):
                ax = fig.add_subplot(2, 2, i + 2)
                hist = calculate_histogram(img, [i])
                plt.plot(hist, color=colors[i][0])
                plt.title(color_channel[i])

        # gray-scale image
        if img.ndim == 2:
            hist_gs = calculate_histogram(img, [0])
            plt.plot(hist_gs, color='k')
            plt.title('gray-scale image')

    else:
        raise Exception('ValueError: image parameter expect path of image as string or a numpy.ndarray')