import numpy as np
from .calculate_psi import psi


def calculate_phi(data):
    """
    :param data: array_like
        An array of images
    Calculate the mean feature of an image.
    phi = gamma - psi
    :return: array_like
        An array of the main feature of each image.
    """

    phi = np.zeros((400, 4096))
    for i in range(400):
        phi[i] = data[i] - psi(data)

    return phi
