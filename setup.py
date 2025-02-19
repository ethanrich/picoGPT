import setuptools
from setuptools import find_packages
from distutils.core import setup
from pathlib import Path


with (Path(__file__).parent / "README.md").open("r") as f:
    long_description = f.read()

with (Path(__file__).parent / "requirements.txt").open("r") as f:
    requirements = [l for l in f.readlines() if not "http" in l]


packages = setuptools.find_namespace_packages(exclude=["tests*", "docs*", "htmlcov*"])

setup(
    name="picoGPT",
    version="0.1.0",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ethan Rich",
    author_email="",
    url="https://github.com/ethanrich/picoGPT.git",
    download_url="https://github.com/ethanrich/picoGPT.git",
    license="MIT",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
