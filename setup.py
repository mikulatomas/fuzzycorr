#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

__author__ = 'Tomáš Mikula'
__email__ = 'mail@tomasmikula.cz'
__version__ = '0.1.0'
__license__ = 'MIT license'

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

# Requirements for end-user
requirements = [
    'numpy>=1.9.2']

# Requirements for test
setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest>=3', ]

setup(
    author=__author__,
    author_email=__email__,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A numpy implementation of Robust Rank Correlation Coefficients",
    install_requires=requirements,
    license=__license__,
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='fuzzycorr, correlation, fuzzy',
    name='fuzzycorr',
    packages=find_packages(include=['fuzzycorr', 'fuzzycorr.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mikulatomas/fuzzycorr',
    version=__version__,
    zip_safe=False,
)
