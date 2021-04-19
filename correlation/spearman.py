from scipy.stats import rankdata
import numpy as np
from .pearson import my_pearson


def spearman_method_process(df):
    """
    Spearman rank correlation process.
    :params
    df: the dataframe
    return: dataframe and rho value.
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


def my_spearman(x, y):
    """
    Calculate the spearman coefficient of the x and y.
    """
    # Rank each x and y
    x_rank = rankdata(x, method='min')
    y_rank = rankdata(y, method='min')

    rho_s = my_pearson(x_rank, y_rank)

    return rho_s



