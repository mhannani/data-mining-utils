from utils.validate_vector import validate_vector
import numpy as np


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
