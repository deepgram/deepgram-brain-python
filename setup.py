from setuptools import find_packages

__author__ = 'jmward'

from distutils.core import setup

setup(name='deepgrambrainclient',
      version='1.0',
      description='Deepgram Brain API client',
      author='Jeff Ward',
      author_email='jeff.ward@deepgram.com',
      classifiers=[
        'Intended Audience :: Developers',
        'Topic :: System :: Networking',
        'Topic :: Office/Business',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords='deepgram transcription audio',
      packages=find_packages(),
      install_requires=['requests'])
