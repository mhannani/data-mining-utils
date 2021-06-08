import numpy as np


def project_img(img, components):
    """
    Proejct the given image in the space formed by components.
    :param img: array_like
        An array like
    :param components: array_like
        An array of retained components
    :return: weights of the projection.
    """
    weights = np.zeros((len(components)))

    for comps in components:
        np.append(weights, np.dot(img, comps))

    return weights


def project_imgs(imgs, components):
    """
    Take a set of images an returns the weights of each one.
    :param components: array_like
        An array of components.
    :param imgs: array_like
    :return: array_like
        Array of weights.
    """

    weights = np.zeros((len(imgs), len(components)))

    for img in imgs:
        np.append(weights, project_img(img, components))

    return weights


