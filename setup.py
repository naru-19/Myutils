import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_install_requires():
    install_requires = [
        'tqdm',
        'numpy',
        'matplotlib',
        'seaborn',
        'pandas',
    ]
    return install_requires

setuptools.setup(
    name="narutils",
    version="0.1.1",
    author="naru-19",
    author_email="narumanage@gmail.com",
    description="You can use narutils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naru-19/Myutils",
    install_requires=get_install_requires(),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
