# FinMesh
---
FinMesh is a python-based package that brings together financial data from various sources in one place for ease of use and distribution. The three main sections of FinMesh are (1) the [IEX REST API][1], (2) data from the [US treasury][2], and (3) the data from the [US Federal Reserve Economic Data][3].

[1]: https://iexcloud.io/docs/api/
[2]: https://www.treasury.gov/resource-center/data-chart-center/digitalstrategy/pages/developer.aspx
[3]: https://fred.stlouisfed.org/

## Purpose
---
The purpose of this package and its sub-packages was originally to practice interacting with API data. With thrid-party API packages there is always the risk of outages or bugs. In building the original IEX wrapper we sought to build something easy to understand and use, that can be updated quickly and accurately.

With the addition of the US Federal data the opportunity arose to create a package that could deliver all sorts of economic and security data from one place. In doing so we hope to create a low-barrier way for beginners to play with large and very useful data sets.

In the future, this package will be updated with new financial and economic APIs. If you know of a low or no cost API that could be incorporated please raise it as an issue and we will work to have it done ASAP.

## Compatability with IEX cloud
---
The name of the function shall be the name of the endpoint.
The function shall accept all variables for a given endpoint using the same variable names per the documentation.
Differences between IEX cloud documentation and this API should be considered errors. Please raise an issue if you notice discrepencies.

## Contact
---
If you would like to reach out, feel free to connect with me one of three ways:

1. [On GitHub][1]

2. [On LinkedIn][2]

3. [Via Email][3]

If there are issues, be it major or semantic, please open an issue on GitHub.


[1]: https://github.com/MichaelPHartmann
[2]: https://www.linkedin.com/in/michael-hartmann/
[3]: MichaelPeterHartmann94@gmail.com
