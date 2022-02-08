"""
For 'python setup.py develop' and 'python setup.py test'
"""
import os
from setuptools import setup, find_packages

ROOT = os.path.dirname(__file__)

setup(
    name="user-interviews",
    version="0.0.1.dev0",
    author='Stefan Grafberger',
    author_email='stefangrafberger@gmail.com',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "mlinspect[dev] @ git+https://github.com/stefan-grafberger/mlinspect.git@"
        "dd94830649c89dc713d38b7b44600edba73f1b46",
        "importnb==0.6.2",
        "matplotlib==3.4.2",
        "tensorflow==2.5.0"
    ],
    license='Apache License 2.0',
    python_requires='==3.9.*',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9'
    ]
)
