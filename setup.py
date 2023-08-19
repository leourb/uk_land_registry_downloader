"""Setup to build the package"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uk_land_registry_downloader",
    version="1.0.0",
    author="Leonardo Urbano",
    author_email="leonardo.urbano87@libero.it",
    description="A client to download data from the HM UK Land Registry using Selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leourb/uk_land_registry_downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)