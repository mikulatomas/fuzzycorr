from fuzzycorr.utils import permutation_pairs
import pytest
import numpy as np
from itertools import permutations as slow_permutations


def test_permutation():
    x = np.array([1, 2, 3])

    assert tuple(slow_permutations(x, 2)) == tuple(
        map(tuple, permutation_pairs(x)))
