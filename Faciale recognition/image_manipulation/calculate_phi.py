import numpy as np
from .calculate_psi import psi


def calculate_phi(data):
    """
    Calculates the array of proper features of each image in the given array, with each column
    represents an image.
    :param data: array_like
        An array of images
    Calculate the mean feature of an image.
    phi = gamma(The original image) - psi(The mean image)
    :return: array_like
        An array of the main feature of each image.
    """

    # The proper features array of the images
    phi = np.zeros((400, 4096))

    # The mean image
    psi_value = psi(data)

    # Calculate the array of the proper feature of each image.
    for i in range(400):
        phi[i] = data[i] - psi_value

    return phi
