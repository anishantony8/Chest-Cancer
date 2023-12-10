import setuptools
import logging

with open("README.md",'r') as f:
    long_description = f.read()
__version__ = "0.0.0"
setuptools.setup(
    name="cnnClassifier",
    version=__version__,
    author="anishantony8",
    author_email="anishantony8gmail.com",
    long_description=long_description,
    url="https://github/anishantony8@gmail.com/cnnClassifier",
    project_urls = {
        "Bug-Tracker":"https://github/anishantony8@gmail.com/cnnClassifier/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)