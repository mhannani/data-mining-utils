from sklearn.datasets import fetch_olivetti_faces


def load_olivetti():
    """
    Load the Olivetti dataset.
    :return: tuple of data and labels.
    """
    olivetti = fetch_olivetti_faces()

    return olivetti.data, olivetti.images
