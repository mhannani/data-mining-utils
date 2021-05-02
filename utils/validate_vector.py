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

    # convert it to ndarray
    u = np.asarray(u)

    # flatten it if flatten is True.
    if flatten:
        u = u.flatten()
    return u
