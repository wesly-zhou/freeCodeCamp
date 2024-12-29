import numpy as np

def get_mean(list):
    means = []
    means.append(list.mean(axis=0).tolist())
    means.append(list.mean(axis=1).tolist())
    means.append(list.mean())
    return means

def get_var(list):
    variances = []
    variances.append(list.var(axis=0).tolist())
    variances.append(list.var(axis=1).tolist())
    variances.append(list.var())
    return variances

def get_sd(list):
    standard_deviations = []
    standard_deviations.append(list.std(axis=0).tolist())
    standard_deviations.append(list.std(axis=1).tolist())
    standard_deviations.append(list.std())
    return standard_deviations

def get_max(list):
    maxes = []
    maxes.append(list.max(axis=0).tolist())
    maxes.append(list.max(axis=1).tolist())
    maxes.append(list.max())
    return maxes

def get_min(list):
    mins = []
    mins.append(list.min(axis=0).tolist())
    mins.append(list.min(axis=1).tolist())
    mins.append(list.min())
    return mins

def get_sum(list):
    sums = []
    sums.append(list.sum(axis=0).tolist())
    sums.append(list.sum(axis=1).tolist())
    sums.append(list.sum())
    return sums

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    calculations = {}
    arr = np.array(list)
    arr = arr.reshape(3, 3)
    calculations['mean'] = get_mean(arr)
    calculations['variance'] = get_var(arr)
    calculations['standard deviation'] = get_sd(arr)
    calculations['max'] = get_max(arr)
    calculations['min'] = get_min(arr)
    calculations['sum'] = get_sum(arr)

    return calculations