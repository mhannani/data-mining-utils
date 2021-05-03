import matplotlib.pyplot as plt


def scatter_it(x, y, x_label, y_label):
    """
    Plot a scatter plot of the provided data.

    :param x: array_like
    :param y: array_like
    :param x_label: x-label of the scatter plot
    :param y_label: y-label of the scatter plot
    :return: None
    """

    fig, ax1 = plt.subplots()
    plt.scatter(x, y)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    plt.show()
