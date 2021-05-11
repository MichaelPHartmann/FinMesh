# FinMesh
---
FinMesh is a python-based package that brings together financial data from various sources in one place for ease of use and distribution. The four main sections of FinMesh are (1) the [IEX REST API][1], (2) data from the [US treasury][2], data from the [US Federal Reserve Economic Data][3], and (4) data from the [SECs EDGAR][4] system.

[1]: https://iexcloud.io/docs/api/
[2]: https://www.treasury.gov/resource-center/data-chart-center/digitalstrategy/pages/developer.aspx
[3]: https://fred.stlouisfed.org/
[4]: https://www.sec.gov/edgar/searchedgar/companysearch.html

## Purpose
---
The purpose of this package and its sub-packages was originally to practice interacting with API data. With third-party API packages there is always the risk of outages or bugs. In building the original IEX wrapper we sought to build something easy to understand and use, that can be updated quickly and accurately.

With the addition of the US Federal data the opportunity arose to create a package that could deliver all sorts of economic and security data from one place. In doing so we hope to create a low-barrier way for beginners to play with large and very useful data sets.

In the future, this package will be updated with new financial and economic APIs. If you know of a low or no cost API that could be incorporated please raise it as an issue and we will work to have it done ASAP.

## Installation
The following dependencies are used in FinMesh:
- OS
- CSV
- JSON
- Requests
- xmltodict
- xml.etree.ElementTree
- webbrowser
- shutil
- BeautifulSoup4

Some APIs require authentication through the use of tokens. These tokens should be set up as environment variables in the bash profile. A great article on how to do this on Mac is available here:

[My Mac OSX Bash Profile](https://natelandau.com/my-mac-osx-bash_profile/)

Click [HERE](https://iexcloud.io/) for your free IEX token.
This token must be stored as IEX_TOKEN in your environment variables.

Click [HERE](https://fred.stlouisfed.org/) for your free FRED token. This token must be stored as FRED_TOKEN in your environment variables.


## Compatibility with IEX cloud
---
The name of the function shall be the name of the endpoint.
The function shall accept all variables for a given endpoint using the same variable names per the documentation.
Differences between IEX cloud documentation and this API should be considered errors. Please raise an issue if you notice discrepancies.

## Contact
---
If you would like to reach out, feel free to connect with me one of three ways:

1. [On GitHub][5]

2. [On LinkedIn][6]

3. [Via Email][7]

If there are issues, be it major or semantic, please open an issue on GitHub.


[5]: https://github.com/MichaelPHartmann
[6]: https://www.linkedin.com/in/michael-hartmann/
[7]: MichaelPeterHartmann94@gmail.com
