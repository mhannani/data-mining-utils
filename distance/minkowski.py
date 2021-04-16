import numpy as np
from math import sqrt, pow


def minkowski(u, v, p):
    """
    Calculates the minkowski distance between two vectors.
    :param u: ndarray-like
    :param v: ndarray-like
    :param p: scalar
    :return: The minkowski distance
    """
    dist = 0
    if p < 1:
        raise ValueError('p must be at least 1')

    # if the the dimensional representation of the image is an ndarray
    if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
        raise ValueError('Please provide two ndarray !')

    else:
        flat_u = u.flatten()
        flat_v = v.flatten()

    dist += pow((sum([pow((u_i - v_i), p) for u_i, v_i in zip(flat_u, flat_v)])), 1/p)
    return dist
