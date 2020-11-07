#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Setup file derived from open-tamil project.
# (C) 2018 Ezhil Language Foundation

from distutils.core import setup
from codecs import open

setup(name='tamilinayavaani',
      version='0.13',
      description='Tamil spell checker',
      author='Tamil Virtual Academy, Neechalkaran, T. Shrinivasan, Ashok Ramachandran, Mani K, Ezhil Language Foundation, et-al',
      author_email='tshrinivasan@gmail.com',
      url='https://github.com/tshrinivasan/Tamilinaiya-Spellchecker.git',
      install_requires=['open-tamil>=0.96'],
      packages=['tamilinayavaani'],
      package_dir={'tamilinayavaani': 'tamilinayavaani'},
      package_data={'tamilinayavaani': ['json/*','koppu/*']},
      license='GPL v2',
      scripts=[],
      platforms='PC,Linux,Mac',
      classifiers=['Natural Language :: Tamil',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4'],
      long_description=open('README.rst','r').read(),
      download_url='https://github.com/Ezhil-Language-Foundation/Tamilinaiya-Spellchecker/archive/v0.12.zip',#pip
      )
