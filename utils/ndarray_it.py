import matplotlib.pyplot as plt
import numpy as np


def ndarray_it(f_img):
    """
    Obtain an ndarray from path or python list.

    :param f_img: a path, python list or ndarray.
    :return: ndarray
    """

    # if it is a path of the image
    if isinstance(f_img, str):
        # read the image
        ndarray = plt.imread(f_img)

    # a python list
    elif isinstance(f_img, list):
        # convert the list into numpy array
        ndarray = np.array(f_img)
    # an ndarray
    elif isinstance(f_img, np.ndarray):
        ndarray = f_img

    else:
        raise Exception('Please provide an ndarray, a path or a python list')

    return ndarray
