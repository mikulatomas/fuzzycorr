import numpy as np

from fuzzycorr import fuzzy_correlation_factory
from fuzzycorr.strict_orderings import classic_ordering
from fuzzycorr.t_norms import godel
from fuzzycorr.utils import permutation_pairs


def crisp_gamma(x, y):
    input_len = x.shape[0]
    index_permutations = permutation_pairs(np.arange(input_len))

    xi, xj = x[index_permutations].T
    yi, yj = y[index_permutations].T

    xixj = classic_ordering(xi, xj)
    yiyj = classic_ordering(yi, yj)
    yjyi = classic_ordering(yj, yi)

    concordant_pairs = np.logical_and(xixj, yiyj)
    discordant_pairs = np.logical_and(xixj, yjyi)

    c = np.sum(concordant_pairs)

    d = np.sum(discordant_pairs)

    return (c - d) / (c + d)


def test_to_classic_gamma():
    ordering = classic_ordering
    fuzzy_corr = fuzzy_correlation_factory(ordering, godel)

    x1 = np.array([12, 2, 1, 12, 2])
    x2 = np.array([1, 4, 7, 1, 0])

    gamma = crisp_gamma(x1, x2)
    corr = fuzzy_corr(x1, x2)

    assert gamma == corr
