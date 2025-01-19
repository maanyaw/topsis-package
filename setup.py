# setup.py
from setuptools import setup, find_packages

setup(
    name='topsis-package',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'openpyxl'
        'twine',  # Required to read Excel files
    ],
    author='maanya',
    author_email='mwalia_be22@thapar.edu',
    description='TOPSIS Decision Making Python Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/maanyaw/topsis-package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
