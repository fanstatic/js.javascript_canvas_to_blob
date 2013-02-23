# -*- coding: utf-8 -*-

"""
Created on 2013-02-23
:author: Andreas Kaiser (disko)
"""

import os

from setuptools import find_packages
from setuptools import setup


version = '2.0.5'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'javascript_canvas_to_blob', 'test_javascript_canvas_to_blob.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.javascript_canvas_to_blob',
    version=version,
    description="Fanstatic packaging of JavaScript Canvas to Blob",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/js.javascript_canvas_to_blob',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'javascript_canvas_to_blob = js.javascript_canvas_to_blob:library',
            ],
        },
    )
