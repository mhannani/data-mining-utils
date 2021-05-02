import numpy as np


def validate_vector(u):
    """
    Validator of a vector.
    :param u: array_like
        An array to be checked and/or converted.
    :return: 1-D array
        An 1-D array
    """

    u = np.asarray(u)
    u = u.flatten()
    return u
