from fuzzycorr import fuzzy_correlation_factory
from fuzzycorr.strict_orderings import lukasiewicz_strict_ordering_factory, product_strict_ordering_factory
from fuzzycorr.t_norms import godel, lukasiewicz, product

import numpy as np
import pytest

test_input_data = []

for tnorm in [godel, product, lukasiewicz]:
    for ordering in [lukasiewicz_strict_ordering_factory, product_strict_ordering_factory]:
        for r in np.arange(0.05, 0.5, 0.1):
            test_input_data.append((ordering, tnorm, r))


@pytest.mark.parametrize("ordering, tnorm, r", test_input_data)
def test_fuzzy_correlation_factory_int(ordering, tnorm, r):
    strict_ordering = ordering(r=r)

    fuzzy_corr = fuzzy_correlation_factory(strict_ordering, tnorm)

    assert callable(fuzzy_corr)

    x = np.array([1, 2, 3])
    y = x

    assert fuzzy_corr(x, y) == pytest.approx(1)


@pytest.mark.parametrize("ordering, tnorm, r", test_input_data)
def test_fuzzy_correlation_factory_float(ordering, tnorm, r):
    strict_ordering = ordering(r=r)

    fuzzy_corr = fuzzy_correlation_factory(strict_ordering, tnorm)

    assert callable(fuzzy_corr)

    x = np.array([0.2, 0.4, 0.6])
    y = x

    assert fuzzy_corr(x, y) == pytest.approx(1)


@pytest.mark.parametrize("ordering, tnorm, r", test_input_data)
def test_fuzzy_correlation_factory_int_flipped(ordering, tnorm, r):
    strict_ordering = ordering(r=r)

    fuzzy_corr = fuzzy_correlation_factory(strict_ordering, tnorm)

    assert callable(fuzzy_corr)

    x = np.array([1, 2, 3])
    y = np.flip(x)

    assert fuzzy_corr(x, y) == pytest.approx(-1)


@pytest.mark.parametrize("ordering, tnorm, r", test_input_data)
def test_fuzzy_correlation_factory_float_flipped(ordering, tnorm, r):
    strict_ordering = ordering(r=r)

    fuzzy_corr = fuzzy_correlation_factory(strict_ordering, tnorm)

    assert callable(fuzzy_corr)

    x = np.array([0.2, 0.4, 0.6])
    y = np.flip(x)

    assert fuzzy_corr(x, y) == pytest.approx(-1)
