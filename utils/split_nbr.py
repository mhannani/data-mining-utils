def split_nbr(number):
    """
    Split the given number into the multiplication of two numbers evenly weighted.
    """
    # if we don't pass to the other greater number `number + 1`
    not_it = False
    if number in [0, 1, 2]:
        return 1, 2, not_it  # one row, two colums

    # use the consecutive number if fails to find two
    # number which has multiplication equal to `number`

    while True:
        # Search for a divider less than its middle
        i = int(number / 2) - 1
        while i > 1:
            if number % i == 0:
                return i, int(number / i), not_it
            i -= 1
        number += 1
        not_it = True
