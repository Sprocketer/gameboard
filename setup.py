from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '{{VERSION_PLACEHOLDER}}'

PACKAGE_NAME = "gameboard"
DESCRIPTION = 'A 3D grid creation library for simulation and games.'
AUTHOR_NAME = "Alex"
AUTHOR_EMAIL = "sprocketerdev@gmail.com"
PROJECT_URL = "https://github.com/Sprocketer/gameboard"
# REQUIRED_PACKAGES = []
PROJECT_KEYWORDS = ['pypi', 'python']
# https://pypi.org/classifiers/
CLASSIFIERS = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url = PROJECT_URL,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    # install_requires=REQUIRED_PACKAGES,
    keywords=PROJECT_KEYWORDS,
    classifiers=CLASSIFIERS
)
