# -*- coding: utf-8 -*-
"""
I18nLibrary translator library for support in robotframework.
"""
import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

with open("README.md", "r", encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

with open(join(CURDIR, 'I18nLibrary', '__init__.py'), encoding='utf-8') as f:
    VERSION = re.search("\n__version__ = '(.*)'", f.read()).group(1)

setup(
    name="robotframework-I18nLibrary",
    version=VERSION,
    author="QA Hive Co.,Ltd",
    author_email="support@qahive.com",
    description="I18nLibrary translator library for support in robotframework.",
    long_description=LONG_DESCRIPTION,
    license="Apache License 2.0",
    url='https://github.com/qahive/robotframework-I18nLibrary',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Framework :: Robot Framework",
    ],
    keywords='robotframework testing automation data-driven qahive',
    platforms='any',
    install_requires=[
        'python-I18nLibrary'
    ],
    python_requires='>3.5',
    test_suite='nose.collector',
    tests_require=['nose', 'parameterized'],
    zip_safe=False,
)
