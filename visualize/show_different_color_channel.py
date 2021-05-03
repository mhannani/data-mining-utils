import matplotlib.pyplot as plt


def show_different_color_channel(path_img):
    """
    Plot different color channel of the given image.
    """

    colors = ['red', 'green', 'blue']
    channel = ' channel'
    color_channel = [color + channel for color in colors]
    rgb_img = plt.imread(path_img)

    # Create a figure
    fig = plt.figure(figsize=(15, 10))

    ax = fig.add_subplot(2, 2, 1)
    plt.imshow(rgb_img)
    plt.title('All color channel')

    for i in range(3):
        ax = fig.add_subplot(2, 2, i + 2)
        plt.imshow(rgb_img[:, :, i], cmap='gray')
        plt.title(color_channel[i])
