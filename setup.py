
from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='oblivious_robots_target_searching',
    version='0.0.4',
    description='This package provides a powerful Playground for designing and testing algorithms for oblivious robots',
    description_content_type='text/plain',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author="Sairyö No Developers",
    author_email='tech@sairyonodevs.in',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Sairyo-No-Developers/oblivious-robots-target-search',
    keywords='oblivious robots target searching graph',
    install_requires=[
          'networkx',
          'matplotlib',
          'uuid',
          'names',
          'pytest'
      ],

)