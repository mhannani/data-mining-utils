import numpy as np
import matplotlib.pyplot as plt
from .. .image_manipulation import project_imgs, project_img


def recognize_face(img, imgs, components, n_faces=3):
    """
    Recognize the given face and return the recognized faces.
    :param n_faces: integer
        Number of images to return.
    :param components: array_like
        An array of components.
    :param img: array_like
        The face to recognized
    :param imgs: array_like
        The dataset of faces
    :return: array_like
        `n_faces` similar faces.
    """

    distance = np.empty(shape=[len(imgs)])
    weight_face = project_img(img, components)
    weights = project_imgs(imgs, components)

    for weight in range(weights):
        delta = weight - weight_face
        np.append(distance, sum(abs(delta)))

    # Show the similar faces
    fig = plt.figure(figsize=(20, 5))

    for i in range(n_faces):
        ax = fig.add_subplot(1, 3, i + 1)
        ax.imshow(imgs[i], cmap='gray')

    return distance.argsort()[:n_faces]
