#!/usr/bin/python
import setuptools

from os import path
requirements_file = path.join(path.dirname(__file__), 'requirements.in')
requirements = open(requirements_file).read().split('\n')

setuptools.setup(
    name='TransE',
    version='1.0',
    url='https://github.com/csbhagav/TransE',
    packages=setuptools.find_packages(),
    install_requires=[], # dependencies specified in requirements.in
    tests_require=[],
    zip_safe=False,
    entry_points=''
)