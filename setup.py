"""
Version naming has been simplified in 2.0 going forward.
Production releases will be MAJOR.MINOR format.
Increments to major are reserved for significant updates.
Increments to minor are available for all new versions
Test releases are MAJOR.MINOR.PATCH format.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "FinMesh",
    version = "2.0.9",
    author = "Michael and Josh Hartmann",
    author_email = "mph101mph@gmail.com",
    description = "A Python wrapper to bring together various financial APIs.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = "Finance, API, DCF, IEX, EDGAR, FRED, interest rates",
    url = "",
    packages=setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3"
    ],
    python_requires = ">3.6",
)
