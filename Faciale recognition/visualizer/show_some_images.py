import matplotlib.pyplot as plt


def show_some_images(imgs):
    """
    Show some images of the given set of images.
    :param imgs: 2D-array.
        An array of images.
    :return: Matplotlib figure
    """

    fig = plt.figure(figsize=(20, 5))

    for i in range(14):
        ax = fig.add_subplot(2, 7, i+1)
        ax.imshow(imgs[i], cmap='gray')
