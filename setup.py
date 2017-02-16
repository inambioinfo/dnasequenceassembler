from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='dnasequencealigner',
    version='0.0.0',
    packages=['dnasequencealigner',],
    license='figures out a unique DNA sequence from overlapping DNA sequences',
    long_description=open('README.txt').read(),
    install_requires=[
        "click",
    ],
    entry_points='''
        [console_scripts]
        align=dnasequencealigner.align:touch
    ''',
)
