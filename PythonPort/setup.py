#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Setup file derived from open-tamil project.
# (C) 2018 Ezhil Language Foundation

from distutils.core import setup
from codecs import open

setup(name='tamilinayavaani',
      version='0.1',
      description='Tamil spell checker',
      author='Tamil Virtual Academy, Neechalkaran, T. Shrinivasan, Ashok Ramachandran, Mani K, Ezhil Language Foundation, et-al',
      author_email='tshrinivasan@gmail.com',
      url='https://github.com/tshrinivasan/Tamilinaiya-Spellchecker.git',
      install_requires=['tamil','tamilsandhi'],
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
      long_description="""
# Spellchecker

# Tamilinaiyam - Pizhaithiruthi

Source: 
http://www.tamilvu.org/ta/content/%E0%AE%A4%E0%AE%AE%E0%AE%BF%E0%AE%B4%E0%AF%8D%E0%AE%95%E0%AF%8D-%E0%AE%95%E0%AE%A3%E0%AE%BF%E0%AE%A9%E0%AE%BF%E0%AE%95%E0%AF%8D-%E0%AE%95%E0%AE%B0%E0%AF%81%E0%AE%B5%E0%AE%BF%E0%AE%95%E0%AE%B3%E0%AF%8D

Thanks to Tamil Virtual Academy, Chennai for releasing ths source code of this application.

License : GPL V2

Check https://commons.wikimedia.org/wiki/File:Tamil-Virtual-Academy-Copyright-Declaration.jpg for license info.""",
      download_url='https://github.com//archive/master.zip',#pip
      )
