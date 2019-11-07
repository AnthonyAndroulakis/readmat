#from distutils.core import setup
from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'readmat',         # How you named your package folder (MyLib)
  #packages = ['readmat'],   # Chose the same as "name"
  scripts=['readmat.py'],
  py_modules=['readmat'],
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Helpful functions for loading .mat MATLAB files into Python. Most data types are supported.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',  # This is important!
  author = 'Anthony Androulakis & stackoverflow users cs01, jpapon, and andyvanee',                   # Type in your name
  author_email = 'aandroulakis@zoho.com',      # Type in your E-Mail
  url = 'https://github.com/AnthonyAndroulakis/readmat',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AnthonyAndroulakis/readmat/archive/v_001.tar.gz',    # I explain this later on
  keywords = ['mat', 'matlab', 'python', 'utilities', 'tool', 'read', 'readmat', 'loadmat', 'load', 'struct', 'structure'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'scipy',
          'numpy'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)
