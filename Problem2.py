import scipy.stats as stats
import numpy as np


def get_data(filename):
    return np.loadtxt(filename)


def get_coordinates(data, each_dist):
    coords, _ = stats.probplot(data, dist=each_dist)
    return coords


def calculate_distance(x, y):
    return ((x - ((x + y) / 2)) ** 2 + (y - ((x + y) / 2)) ** 2) ** 0.5



def find_dist(data):
    return (min(data, key=data.get), data[min(data, key=data.get)])


def main(data_file):
    """
    Input a csv file and return distribution type, the error corresponding to the distribution type (e.g. return ('norm', 0.32))
    :param: *.csv file name (str)
    :return: (str, float)
    """
    data = get_data(data_file)
    dists = ("norm", "expon", "uniform", "wald")
    sum_err = [0] * 4
    for ind, each_dist in enumerate(dists):
        X, Y = get_coordinates(data, each_dist)
        for x, y in zip(X, Y):
            sum_err[ind] += calculate_distance(x, y)
    return find_dist(dict(zip(dists, sum_err)))


if __name__ == "__main__":
    for each_dataset in [
        "sample_norm.csv",
        "sample_expon.csv",
        "sample_uniform.csv",
        "sample_wald.csv",
        "distA.csv",
        "distB.csv",
        "distC.csv",
    ]:
        print(main(each_dataset))
