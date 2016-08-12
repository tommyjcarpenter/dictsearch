from distutils.core import setup
from setuptools import setup, find_packages

setup(
      name = "dictsearch",
      version = "3.1.0",
      author = "Tommy Carpenter",
      author_email = "tommyjcarpenter@gmail.com",
      url = "https://github.com/tommyjcarpenter/dictsearch",
      description = "A tool for iterating dictionaries as trees and printing all leaf nodes at some path",
      license = "MIT License",
      packages=find_packages(),
      install_requires = ['pytest']
     )
