
"""
Copyright 2016 Deepgram
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from setuptools import find_packages, setup
import os

__author__ = 'jmward'

################################################################################
def get_version():
	""" Gets the current version of the package.
	"""
	version_py = os.path.join(os.path.dirname(__file__), 'brain', 'version.py')
	with open(version_py, 'r') as fh:
		for line in fh:
			if line.startswith('__version__'):
				return line.split('=')[-1].strip().replace('"', '')
	raise ValueError('Failed to parse version from: {}'.format(version_py))

################################################################################

setup(name='brain',
      version=get_version(),
      description='Deepgram Brain API client',
      author='Jeff Ward',
      license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
      copyright='Copyright (c)2017 Deepgram',
      author_email='jeff.ward@deepgram.com',
      url='https://github.com/deepgram/deepgram-brain-python',
      classifiers=[
        'Intended Audience :: Developers',
        'Topic :: System :: Networking',
        'Topic :: Office/Business',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
      ],
      keywords=['deepgram', 'transcription', 'audio', 'deep learning', 'speech', 'awesome'],
      packages=find_packages(),
      install_requires=['requests'])


