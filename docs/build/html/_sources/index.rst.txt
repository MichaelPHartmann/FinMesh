.. FinMesh documentation master file, created by
   sphinx-quickstart on Sat Sep 18 15:51:05 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FinMesh's documentation!
===================================

FinMesh is a python-based package that brings together financial data from various sources in one place for ease of use and distribution.
The four main sections of FinMesh are (1) the `IEX REST API`_, (2) data from the `US treasury`_, data from the `US Federal Reserve Economic Data`_, and (4) data from the `SECs EDGAR`_ system.

.. _IEX REST API: https://iexcloud.io/docs/api/
.. _US treasury: https://www.treasury.gov/resource-center/data-chart-center/digitalstrategy/pages/developer.aspx
.. _US Federal Reserve Economic Data: https://fred.stlouisfed.org/
.. _SECs EDGAR: https://www.sec.gov/edgar/searchedgar/companysearch.html

The purpose of this package and its sub-packages was originally to practice interacting with API data. With third-party API packages there is always the risk of outages or bugs.
In building the original IEX wrapper we sought to build something easy to understand and use, that can be updated quickly and accurately.

With the addition of the US Federal data the opportunity arose to create a package that could deliver all sorts of economic and security data from one place.
In doing so we hope to create a low-barrier way for beginners to play with large and very useful data sets.

In the future, this package will be updated with new financial and economic APIs.
If you know of a low or no cost API that could be incorporated please raise it as an issue and we will work to have it done ASAP.

.. toctree::
   :maxdepth: 3
   :caption: Table of Contents:

   install
   iexstockclass
   iex


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
