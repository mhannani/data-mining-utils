import sys
sys.path.append("..")
from array_manipulation.transpose_array import sum_over_columns


def calculate_psi(face_image):
    """
    Calculate the mean image.
    :param face_image: array_like
    :return:
    """
    mean_array = sum_over_columns(face_image)
    num_images = face_image.shape[0]

    psi = mean_array * (1/num_images)

    return psi




