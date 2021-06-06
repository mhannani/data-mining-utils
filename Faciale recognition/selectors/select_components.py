def select_components(n_comps, pca):
    """
    Select the `n_comps` to retain for the projection.
    :param pca: the trained model
    :param n_comps:
    :return: array_like
        An array of the selected components
    """
    retained_comps = []
    for i in range(n_comps):
        retained_comps = retained_comps.append(pca.components_[i])

    return retained_comps
