from scipy.stats import rankdata
import numpy as np


class Correlation:
    """
    Class of some correlation measures.
    """

    @staticmethod
    def pearson(x, y):
        """
        Compute the pearson's coefficient of the given data.
        :param x: array_like
            Array of features.
        :param y: array_like
            Array of labels.
        """

        # Calculate the mean of x and y
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        # calculate the standard deviation of x and y
        x_std = np.sqrt(np.sum(np.power((x - x_mean), 2)))
        y_std = np.sqrt(np.sum(np.power((y - y_mean), 2)))

        # The co-variance of x and y
        cov__x__y = np.sum((x - x_mean) * (y - y_mean))

        # The pearson's rank correlation
        rho = cov__x__y / (x_std * y_std)

        return rho

    @staticmethod
    def spearman_method_process(df):
        """
        Spearman rank correlation process.
        :param df: Dataframe_like
        :return: tuple
            Tuple of dataframe and rho value.
        """

        iq = df['IQ']
        n = len(iq)
        tv_per_hour = df['tv per hour']
        x_rank = len(iq) - rankdata(iq) + 1
        y_rank = len(tv_per_hour) - rankdata(tv_per_hour) + 1
        df['x rank'] = x_rank
        df['y rank'] = y_rank
        df['d'] = x_rank - y_rank
        df['d^2'] = df['d'] ** 2
        sum_of_it = np.sum(df['d^2'])
        rho = 1 - 6 * sum_of_it / (n * (n ** 2 - 1))

        return df, rho

    @staticmethod
    def spearman(x, y):
        """
        Calculate the spearman coefficient of the x and y.
        """
        # Rank each x and y
        x_rank = rankdata(x, method='min')
        y_rank = rankdata(y, method='min')

        rho_s = Correlation.pearson(x_rank, y_rank)

        return rho_s
