import numpy as np
from math import sqrt, pow


def euclidean(u, v):
    """
    Calculate the euclidean distance between two images.
    :param u: The first image as ndarray.
    :param v: The second as ndarray.
    :return: The euclidean distance.
    """
    dist = 0
    # if the the dimensional representation of the image is an ndarray
    if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
        raise ValueError('Please provide two ndarray !')
    else:
        flat_u = u.flatten()
        flat_v = v.flatten()

    dist += sqrt(sum([pow((u_i - v_i), 2) for u_i, v_i in zip(flat_u, flat_v)]))

    return dist









