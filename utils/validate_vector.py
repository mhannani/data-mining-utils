import numpy as np


def validate_vector(u, flatten=True):
    """
    Validate and/or flatten a vector.
    :param u: array_like
        An array to be checked and/or converted.
    :param flatten: boolean
        A boolean to specify whether the array should be flattened or not.
    :return: 1-D array
        An 1-D array
    """

    u = np.asarray(u)
    if flatten:
        u = u.flatten()
    return u
