#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def setup_package():
    setup(
        version="0.1.5",
        packages=["farneback3d"],
        package_data={"farneback3d": ["*.cu"]},
        setup_requires=[],
        install_requires=["numpy", "pycuda", "scipy", "tqdm"],
        extra_require={"docs": ["sphinx"], "test": ["pytest-cov"]},
    )


if __name__ == "__main__":
    setup_package()
