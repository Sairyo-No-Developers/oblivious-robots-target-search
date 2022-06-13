
import re
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSIONFILE="src/oblivious_robots_target_searching/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name='oblivious_robots_target_searching',
    version=verstr,
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
          'scipy',
          'networkx',
          'matplotlib',
          'uuid',
          'names',
          'pytest',
          'pyqt5'
      ],
    scripts=['bin/oblivious-robots.bat', 'bin/oblivious-robots']

)
