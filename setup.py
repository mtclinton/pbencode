from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pbencode",
    version="1.0.0",
    author="mtclinton",
    author_email="max@mtclinton.com",
    description='Python bencoder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5',
)
