from setuptools import setup, find_packages

setup(
    name="dictsearch",
    version="3.2.0",
    author="Tommy Carpenter",
    author_email="tommyjcarpenter@gmail.com",
    url="https://github.com/tommyjcarpenter/dictsearch",
    description="A tool for iterating dictionaries as trees and printing all leaf nodes at some path",
    license="MIT License",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
    ],
)
