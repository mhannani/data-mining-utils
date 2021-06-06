import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np


def show_eigen_faces(imgs, n_components):
    """
    Show some images from the eigen faces.
    :return: None
    """

    pca = PCA(n_components=n_components, svd_solver='randomized', whiten=True)
    pca.fit(imgs)
    fig = plt.figure(figsize=(20, 5))

    for i in range(min(n_components, 14)):
        ax = fig.add_subplot(2, 7, i + 1)
        ax.imshow(pca.components_[i].reshape(64, 64), cmap='gray')
