import numpy as np
import matplotlib.pyplot as plt


def norm_histogram(histogram):
    return [n / (sum(histogram)) for n in histogram]


def compute_j(histogram, bin_width, num_samples):
    return (2 - (num_samples + 1) * sum(p ** 2 for p in norm_histogram(histogram))) / ((num_samples - 1) * bin_width)

def sweep_n(data, min_val, max_val, min_bins, max_bins):
    results = []

    for bins in range(min_bins, max_bins + 1):
        n, _, _ = plt.hist(data, bins=bins, range=(min_val, max_val))
        results.append(compute_j(n, (max_val - min_val) / bins, len(data)))

    return results

def find_min(l):
    return {i: l[i] for i in (sorted(range(len(l)), key=lambda i: l[i])[:3])}


if __name__ == "__main__":
    data = np.loadtxt("input.txt") 
    lo = min(data)
    hi = max(data)
    bin_l = 1
    bin_h = 100
    js = sweep_n(data, lo, hi, bin_l, bin_h)
    """
    the values bin_l and bin_h represent the lower and higher bound of the range of bins.
    They will change when we test your code and you should be mindful of that.
    """
    print(find_min(js))
