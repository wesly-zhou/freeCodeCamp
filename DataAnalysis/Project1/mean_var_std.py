import numpy as np

def get_mean(list):
    """
    Get the mean of the rows, columns, and elements in a 3 x 3 matrix.
    """
    means = []
    means.append(list.mean(axis=0).tolist())
    means.append(list.mean(axis=1).tolist())
    means.append(list.mean())
    return means

def get_var(list):
    """
    Get the variance of the rows, columns, and elements in a 3 x 3 matrix.
    """
    variances = []
    variances.append(list.var(axis=0).tolist())
    variances.append(list.var(axis=1).tolist())
    variances.append(list.var())
    return variances

def get_sd(list):
    """
    Get the standard deviation of the rows, columns, and elements in a 3 x 3 
    matrix.
    """
    standard_deviations = []
    standard_deviations.append(list.std(axis=0).tolist())
    standard_deviations.append(list.std(axis=1).tolist())
    standard_deviations.append(list.std())
    return standard_deviations

def get_max(list):
    """
    Get the max of the rows, columns, and elements in a 3 x 3 matrix.
    """
    maxes = []
    maxes.append(list.max(axis=0).tolist())
    maxes.append(list.max(axis=1).tolist())
    maxes.append(list.max())
    return maxes

def get_min(list):
    """
    Get the min of the rows, columns, and elements in a 3 x 3 matrix.
    """
    mins = []
    mins.append(list.min(axis=0).tolist())
    mins.append(list.min(axis=1).tolist())
    mins.append(list.min())
    return mins

def get_sum(list):
    """
    Get the sum of the rows, columns, and elements in a 3 x 3 matrix.
    """
    sums = []
    sums.append(list.sum(axis=0).tolist())
    sums.append(list.sum(axis=1).tolist())
    sums.append(list.sum())
    return sums

def calculate(list):
    """
    Get the mean, variance, standard deviation, max, min, and sum of the rows, 
    columns, and elements in a 3 x 3 matrix.
    """
    # Raise an error if there are less than 9 elements in the list
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    calculations = {}

    # Create a 3x3 Numpy array from the list
    arr = np.array(list)
    arr = arr.reshape(3, 3)

    # Fill in the calculations dict
    calculations['mean'] = get_mean(arr)
    calculations['variance'] = get_var(arr)
    calculations['standard deviation'] = get_sd(arr)
    calculations['max'] = get_max(arr)
    calculations['min'] = get_min(arr)
    calculations['sum'] = get_sum(arr)

    return calculations