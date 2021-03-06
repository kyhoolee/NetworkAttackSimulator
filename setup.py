import sys
from setuptools import setup

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "The Network Attack Simulator repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

setup(name='nasim',
      version='0.5',
      install_requires=[
        'numpy',
        'networkx',
        'matplotlib',
        'pyyaml'
      ],
      description="A simple and fast simulator for remote network penetration testing",
      author="Jonathon Schwartz")
