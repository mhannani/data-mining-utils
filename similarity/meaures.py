import numpy as np
from utils.validate_vector import validate_vector
from utils.tr_color_2_bi_img import tr_color_2_bi_img


class Measures:
    """
    Class containing some similarity measures.
    """

    @staticmethod
    def jaccard(u, v, as_binary=True):
        """
        Compute the Jaccard similarity between two boolean arrays.

        M_{11} represents the total number of attributes where A and B both have a value of 1.
        M_{01} represents the total number of attributes where the attribute of A is 0 and the attribute of B is 1.
        M_{10} represents the total number of attributes where the attribute of A is 1 and the attribute of B is 0.
        M_{00} represents the total number of attributes where A and B both have a value of 0.

        J = M_{11} / (M_{01} + M_{10} + M_{11})

        :param u: array_like
        :param v: array_like
        :param as_binary: boolean
            If True the function gonna treat element on the array as boolean (convert them if needed)
            else it gonna treat them as integer value and compute the similarity
            measure using array values.
        :return: double
            The jaccard similarity measure value.
        """

        # Check the vector validity or convert it into vector
        u = validate_vector(u, flatten=False)
        v = validate_vector(v, flatten=False)

        # convert array into binary
        if as_binary:
            # check if the array contains only binary elements(`0`, `1`, `True` or 'False`)
            u_is_bi = np.array_equal(u, u.astype(bool))
            v_is_bi = np.array_equal(v, v.astype(bool))

            # convert array into binary array if not already.
            if not u_is_bi:
                u = tr_color_2_bi_img(u, 175)
            if not v_is_bi:
                v = tr_color_2_bi_img(v, 175)

        # convert into 1-D array if needed
        u = u.flatten().astype(int)
        v = v.flatten().astype(int)

        # True positive count
        m_11 = np.double(np.bitwise_and(u, v).sum())

        # True positive and False positive and True negative count
        m_01__m_10__m_11 = np.double(np.bitwise_or(u, v).sum())

        # compute jaccard measure
        j_score = m_11 / m_01__m_10__m_11

        return j_score

    @staticmethod
    def cosine(u, v):
        """
        Compute the cosine measures between two given images.
        :param u: array-like
            An array representing the image.
        :param v: array-like
            An array representing the image.
        :return: double
            The cosine measure value.
        """

        u = validate_vector(u)
        v = validate_vector(v)

        cosine_similarity = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))

        return cosine_similarity

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
