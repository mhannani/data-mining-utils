from correlation.correlation_measures import Correlation
from histogram.compare_img_hist import compare_img_hist
from utils.max_val_dict import max_val_dict
from utils.min_val_dict import min_val_dict


class Similar:
    """
    Encapsulates some helper function to search for similar images from a set of images
    """

    @staticmethod
    def search_n_similar_images(images, image, n):
        """
        Find similar images of the given one.

        :param images: array_like
            Array of images
        :param image: array_like
            An image to search for its similar
        :param n: integer
            Number of first similar to yield.
        :return: tuple
            A tuple of containing similar images of image given as argument and their spearman correlation value.
        """

        # Holds the current iteration value.
        iteration = 0

        # dictionary will hold values.
        dic_values = {}

        # holds array of similar images
        similar_images = []

        # store the spearman value of each images from the set with the given image.
        for img in images:
            # compute the spearman correlation between the current image and the given image.
            spr_val = abs(Correlation.pearson(img, image))

            # # avoid storing the spearman correlation value with its duplicate image.
            # if spr_val < 1.0:
            #     # dictionary stores the spearman value with its index.
            #     dic_values[iteration] = spr_val
            dic_values[iteration] = spr_val
            iteration += 1

        # look for n similar images
        dict_n_imgs = {}
        dump_iter = n

        while dump_iter > 0 and len(dic_values) != 0:
            # key with maximum value
            key_max_value = max_val_dict(dic_values)

            dict_n_imgs[key_max_value] = dic_values[key_max_value]
            dic_values.pop(key_max_value)
            dump_iter -= 1

        # Stores the spearman values of n most similar images as a list
        spearman_n_values = list(dict_n_imgs.values())

        # The indices of similar images.
        n_keys_similar_images = list(dict_n_imgs.keys())

        # corresponding images
        for key in n_keys_similar_images:
            similar_images.append(images[key])

        return similar_images, spearman_n_values

    @staticmethod
    def search_n_similar_images_by_hist(images, image, n):
        """
        Find similar images of the given one by minimizing the difference of their histogram.

        :param images: array_like
            Array of images
        :param image: array_like
            An image to search for its similar
        :param n: integer
            Number of first similar to yield.
        :return: tuple
            A tuple of containing similar images of image given as argument and their histogram difference value.
        """

        # Holds the current iteration value.
        iteration = 0

        # dictionary will hold difference values.
        dic_values = {}

        # holds array of similar images
        similar_images = []

        # store the difference between the two images.
        for img in images:
            # compute the histogram of the current image and the given image.
            hist_diff_val = compare_img_hist(img, image)
            dic_values[iteration] = hist_diff_val
            iteration += 1

        # look for n similar images
        dict_n_imgs = {}
        dump_iter = n

        while dump_iter > 0 and len(dic_values) != 0:
            # key with maximum value
            key_min_value = min_val_dict(dic_values)

            dict_n_imgs[key_min_value] = dic_values[key_min_value]
            dic_values.pop(key_min_value)
            dump_iter -= 1

        # Stores the histogram difference values of n most similar images with the input image as a list
        hist__n_values = list(dict_n_imgs.values())

        # The indices of similar images.
        n_keys_similar_images = list(dict_n_imgs.keys())

        # corresponding images
        for key in n_keys_similar_images:
            similar_images.append(images[key])

        return similar_images, hist__n_values
