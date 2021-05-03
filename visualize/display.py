import matplotlib.pyplot as plt

from utils.split_nbr import split_nbr


def display_similar_images(x, y, nbr_imgs):
    """
    Display similar images of our data.\
    :params
    :X dataframe-like of data.
        Data with each pixel of the instances.
    :n_row integer
        Number of rows of the subplot.
    :n_col integer
        Number of cols of the subplot.
    """
    # compute the number of rows and columns
    fig = plt.figure(figsize=(18, 10))

    # number of rows and cols sufficient to show all images.
    nrows, ncols, cond = split_nbr(nbr_imgs)
    if cond:
        nbr_imgs = ncols * nrows - 1

    for i in range(nbr_imgs):
        ax = fig.add_subplot(nrows, ncols, i + 1)  # A non-zero value is required.
        if i == 0:
            ax.text(0, 3, s='Initial image', color='white', fontsize=10)

        plt.imshow(x[i])
        plt.title(y[i])
