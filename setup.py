# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    'requests'
]

test_requirements = [
    'coverage', 'wheel', 'pytest', 'requests_mock'
]

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 3 - Alpha"
]

setup(
    name="pytaravis",
    author="anuwataravis",
    author_email="email@anuwataravis.com",
    description="anuwataravis python personal tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anuwatavis/pytaravis.git",
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
    tests_require=test_requirements,
    classifiers=classifiers
)
