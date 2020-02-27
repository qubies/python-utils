from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call

setup(
    name='myutils',
    version='1.0.1',
    url='https://github.com/qubies/python-utils',
    author='Tobias Renwick',
    author_email='tobias@renwick.tech',
    description='Some utility functions I reuse',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[])
