import numpy as np

def my_pearson(x, y):
    """
    Compute the pearson's coefficient of the given data.
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
