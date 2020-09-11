# fuzzycorr
A ``numpy`` implementation of Robust Rank Correlation Coefficients (fuzzy correlation) based on paper:

```
Bodenhofer, U., and F. Klawonn. "Robust rank correlation coefficients on the basis of fuzzy." Mathware & Soft Computing 15.1 (2008): 5-20.
```

This implementation is experimental and need future optimization and testing.

## Installation

This package will be avaliable soon on ``pip``.

## Basic usage

```python
from fuzzycorr import fuzzy_correlation_factory
from fuzzycorr.strict_orderings import lukasiewicz_strict_ordering_factory
from fuzzycorr.t_norms import godel

# create strict fuzzy ordering or supply own one
strict_ordering = lukasiewicz_strict_ordering_factory(r=0.2)

# create fuzzy correlation function with tnorm
fuzzy_corr = fuzzy_correlation_factory(godel)

# load data
x = np.random.random(10)
y = np.random.random(10)

# calculate fuzzy correlation
fuzzy_corr(x, y)
```

Visit [example Jupiter Notebook](example.ipynb).

## Development

Clone this repository to the folder, then:

```bash
# create virtualenv (optional)
$ mkvirtualenv fuzzycorr -p python3

#if is not actived (optional)
$ workon fuzzycorr 

$ pip install -e .

$ python setup.py test
```