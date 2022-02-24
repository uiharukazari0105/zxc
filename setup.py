#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", encoding="utf-8", mode="r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zxc",
    version="1.0",
    author="初春飾利",
    author_email="glf20041128@163.com",
    license="MIT",
    description="常用工具集合",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uiharukazari0105/zxc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "datetime", "pyautogui", "pywin32", "pandas", "openpyxl", "opencv-python", "borax"
    ],
    python_requires=">=3",
)
