import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np


def pca_vs_variance(imgs, variance=0.95):
    """
    Plot the pca versus variance to choose accurately the number of components.
    :param variance: double
        The variance.
    :param imgs: array_like
        Array of images..
    :return The trained model.
    """

    # Fit the model
    pca = PCA().fit(imgs)
    y = np.cumsum(pca.explained_variance_ratio_)
    plt.axhline(y=variance, color='r', linestyle='-')
    plt.text(0.1, variance + 0.02, f'{variance * 100}% cut-off threshold', color='red', fontsize=10)
    plt.plot(y, linestyle='--', color='b')
    plt.xlabel('number of components')
    plt.ylabel('cumulative explained variance')

    return pca
