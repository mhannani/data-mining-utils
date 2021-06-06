def calculate_gamma_of_array(arr):
    """
    Calculate the sum over columns in a 2D-array.
    :param arr: array_like
        An array to be transposed.
    :return: An_array
        1D-array of the summed columns
    """

    sum_of_gammas = arr.sum(axis=0)
    return sum_of_gammas


def gamma(arr):
    """
    Takes an image and return a vector.
    :param arr: array_like
        An image as numpy_array.
    :return: array_like
        1D_array
    """

    return arr.flatten()
