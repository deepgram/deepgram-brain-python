from setuptools import find_packages, setup

__author__ = 'jmward'

setup(name='brain',
      version='1.0', # use an version include
      description='Deepgram Brain API client',
      author='Jeff Ward',
      license='apache2', # check KUR for license file
      copyright='Copyright (c)2017 Deepgram',
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
