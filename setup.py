from setuptools import setup
from codecs import open
from os import path

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='rapydmain',
    packages=['rapydmain'],
    install_requires=[],
    version='1.0.0',

    url='https://github.com/aznuii',
    author='aznuii',
    author_email='aaz.nuii@gmail.com',

    keywords='rapydmain',
    description='rapydmain is framework for python batch script.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)
