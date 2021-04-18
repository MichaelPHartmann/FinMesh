import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "FinMesh",
    version = "1.8.4",
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
