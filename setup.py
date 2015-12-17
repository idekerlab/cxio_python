#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Setup script for cxio-python library

To install, run:

python setup.py install

"""

from setuptools import setup, find_packages

setup(
    name='cxio',
    version='0.3.0',
    description='Utility to parse CX JSON streams',
    long_description='Utility collection to use CX JSON in Python.',
    author='Christian Zmasek',
    author_email='cmzmasek@ucsd.edu',
    url='https://github.com/idekerlab/cxio_python',
    license='MIT License',
    install_requires=[
        'ijson'
    ],
    keywords=['data visualization', 'visualization', 'cytoscape',
              'bioinformatics', 'graph', 'network'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    test_suite='test',
    packages=find_packages(),
    include_package_data=True,
)
