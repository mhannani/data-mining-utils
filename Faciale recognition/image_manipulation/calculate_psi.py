from .calculate_gamma import calculate_gamma_of_array


def psi(face_image):
    """
    Calculate the mean image.
    :param face_image: array_like
    :return:
    """
    mean_array = calculate_gamma_of_array(face_image)
    num_images = face_image.shape[0]

    psi_val = mean_array * (1/num_images)

    return psi_val




