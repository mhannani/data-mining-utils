import matplotlib.pyplot as plt


def scatter_it(x, y, x_label, y_label):
    """
    plot a scatter plot of the provided data.
    params:
    x: x-axis
    y: y-axis
    x_label: x-label of the scatter plot
    y_label: y-label of the scatter plot
    return: NULL
    """

    fig, ax1 = plt.subplots()
    plt.scatter(x, y)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)
    plt.show()
