from math import sqrt, pow


class Distances:
    """
    Class contains some distance measures.
    """

    @staticmethod
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

        dist += sqrt(sum([pow((int(u_i) - int(v_i)), 2) for u_i, v_i in zip(flat_u, flat_v)]))

        return dist

    @staticmethod
    def manhattan(u, v):
        """
        Calculates the manhattan distance.
        :param u: ndarray-like
        :param v: ndarray-like
        :return: the manhattan distance
        """
        dist = 0

        if not isinstance(u, np.ndarray) or not isinstance(v, np.ndarray):
            raise ValueError('Please provide two ndarray !')
        else:
            flat_u = u.flatten()
            flat_v = v.flatten()

        for u_i, v_i in zip(flat_u, flat_v):
            dist += sum([abs(int(u_i) - int(v_i))])

        return dist

    @staticmethod
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

        dist += pow((sum([pow((int(u_i) - int(v_i)), p) for u_i, v_i in zip(flat_u, flat_v)])), 1 / p)
        return dist

