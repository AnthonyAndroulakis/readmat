from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'readmat',
  scripts=['readmat.py'],
  py_modules=['readmat'],
  version = '0.0.1',      
  license='MIT',        
  description = 'Helpful functions for loading .mat MATLAB files into Python. Most data types are supported.',   
  long_description=long_description,
  long_description_content_type='text/markdown',  
  author = 'Anthony Androulakis & stackoverflow users cs01, jpapon, and andyvanee',                   
  author_email = 'aandroulakis@zoho.com',      
  url = 'https://github.com/AnthonyAndroulakis/readmat',   
  download_url = 'https://github.com/AnthonyAndroulakis/readmat/archive/v_001.tar.gz',    
  keywords = ['mat', 'matlab', 'python', 'utilities', 'tool', 'read', 'readmat', 'loadmat', 'load', 'struct', 'structure'],   
  install_requires=[            
          'scipy',
          'numpy'
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
  ],
)
