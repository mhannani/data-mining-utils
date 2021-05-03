def max_val_dict(dictionary):
    """
    Find out the maximum value of the given dictionary.
    :param dictionary: a dictionary
        A dictionary where to find the greater value.
    :return integer
        The key that corresponds to the greater value.
    """

    values = list(dictionary.values())
    keys = list(dictionary.keys())
    return keys[values.index(max(values))]
