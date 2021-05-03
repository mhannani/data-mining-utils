def min_val_dict(dictionary):
    """
    Find out the minimum value of the given dictionary.
    :param dictionary: a dictionary
        A dictionary where to find the smaller value.
    :return integer
        The key that corresponds to the smaller value.
    """

    values = list(dictionary.values())
    keys = list(dictionary.keys())
    return keys[values.index(min(values))]
