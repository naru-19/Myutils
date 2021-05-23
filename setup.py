import setuptools
from pip.req import parse_requirements
import sys, os, pip

requirements = [
    str(requirement.req)
    for requirement in parse_requirements('requirements.txt', session = pip.download.PipSession())
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="narutils",
    version="0.1.0",
    author="naru-19",
    author_email="narumanage@gmail.com",
    description="You can use narutils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naru-19/Myutils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
    python_requires='>=2.7',
)
