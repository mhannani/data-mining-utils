def calculate_gamma_of_array(arr):
    """
    Calculate the sum over columns in a 2D-array.
    :param arr: array_like
        An array to be transposed.
    :return: An_array
        1D-array of the summed columns
    """

    gamma_of_arr = arr.sum(axis=0)
    return gamma_of_arr
