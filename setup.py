from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='dnasequenceassembler',
    version='0.0.0',
    packages=['dnasequenceassembler',],
    license='figures out a unique DNA sequence from overlapping DNA sequences',
    long_description=open('README.txt').read(),
    install_requires=['six>=1.7',
        "click",
        "pytest",
        "mock"
    ],
    entry_points='''
        [console_scripts]
        assemble=dnasequenceassembler.cmd:touch
    ''',
)
