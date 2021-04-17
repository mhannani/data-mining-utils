import numpy as np


def manhattan(u, v):
    """
    Calculates the manhattan distance.
    :param u: ndarray-like
    :param v: ndarray-like
    :return: the manhattan distance
    """
    dist = 0
    (X_train, y_train), (X_test, y_test) = keras.datasets.cifar10.load_data()

    if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
        raise ValueError('Please provide two ndarray !')
    else:
        flat_u = u.flatten()
        flat_v = v.flatten()

    for u_i, v_i in zip(flat_u, flat_v):
        dist += sum([abs(int(u_i) - int(v_i))])

    return dist
