def sum_over_columns(arr):
    """
    Calculate the sum over columns in a 2D-array.
    :param arr: array_like
        An array to be transposed.
    :return: An_array
        1D-array of the summed columns
    """
    array_sum_columns = arr.sum(axis=0)
    return array_sum_columns
