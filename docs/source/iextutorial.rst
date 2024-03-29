..
  Updated 25 August 2022

Accessing IEX Cloud
###################

These tutorials are meant for those who are new to programming, and cover each step fairly thoroughly.
If you are experienced in Python, the docs are more in depth and cover the actual methods available.

Using the IEXStock Class to Access Data
=======================================
The easiest way to access data for a particular stock (or group of stocks) is using the IEXStock class.
It stores relevant information like ticker, date, and data period preferences so you can request data and get it in a single line.
It also stores all the requests you've made as dynamic class attributes, meaning you can save on credits.
You can output data as JSON or as Pandas, and then through Pandas as either excel or csv format.

The IEXStock class is contained in the ``iex`` directory's ``__init__`` file so there is no need to specify further than the directory level.

Importing and Initializing
^^^^^^^^^^^^^^^^^^^^^^^^^^

When you attach the variable name ``AAPL`` to the class, you are doing what is called initializing the class.
When you initialize a class, sometimes you are required to input some details about the class. These are called arguments.
The IEXStock class only requires a single argument, and that is ``'ticker'``. This is the ticker or symbol of the stock as a string.

The program will tell you if you forgot an argument and that will look something like this:

  >>> AAPL = IEXStock()
  TypeError: __init__() missing 1 required positional argument: 'ticker'

In these examples I'll look at three ways one can get FinMesh into their code.
They all accomplish the same thing.

You can import the whole package and call the directory and class:

  >>> import FinMesh
  >>> AAPL = FinMesh.iex.IEXStock('AAPL')

You can import the specific IEX module and call the class:

  >>> from FinMesh import iex
  >>> AAPL = iex.IEXStock('AAPL')

Or you can import just the class and save yourself some typing:

  >>> from FinMesh.iex import IEXStock
  >>> AAPL = IEXStock('AAPL')

Calling Methods - The Basics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you have initialized a new class with the ticker of the stock you want to look at, you can start requesting data.
Each grouping of data (in API speak we would call them endpoints) uses a function to gather and optionally format the data.
The naming of all the methods in the IEXStock class follow two rigid rules:

1. All method names will match as closely as possible with their names according to IEX Cloud documentation, with all spaces as underscores

and

2. All data request methods under the IEXStock class have the prefix '\get_'

Here we will request some key stats about the company and their latest quarterly balance sheet.

  >>> AAPL.get_key_stats()
  # A whole bunch of JSON containing the keys and values from the Key Stats endpoint

  >>> AAPL.get_balance_sheet()
  # A whole bunch of JSON containing the keys and values from the latest balance sheet

These methods will return some nice JSON data, but we don't always want JSON data. Pandas is the solution for that.
Pandas takes data and formats it into ``dataframes``, otherwise known as tables.
This makes it easier to work with in Python and export to Excel.
If you want to output a Pandas dataframe, simply specify the output:

  >>> AAPL.get_key_stats(ouput='pandas')
  # A nice dataframe containing the keys and values from the Key Stats endpoint

Class Attributes
^^^^^^^^^^^^^^^^

Every time you call a method, you are making a request to the IEX Cloud API, thus costing you credits.
Even the lowest teir has more than enough credits to work with small projects, but as soon as you want to start gathering data on a larger scale, you will find yourself needing more credits..

One limited solution to this is keeping the responses from the methods as a class attribute.
A class attribute is basically just a characteristic of the class. For example, an attribute of moles is they live undergound, and an attribute of our example IEXStock class is the key stats data.

When you call a method, the result will automatically be assigned to an attribute of the same name, minus the '\get' prefix.
You call it with the class name and no parenthesis.

  >>> AAPL.key_stats
  # A nice dataframe containing the keys and values from the Key Stats endpoint

  >>> AAPL.balance_sheet
  # A whole bunch of JSON containing the keys and values from the latest balance sheet

Notice that when we call the attributes they return different data types.
That is because the attribute will be whatever output type (JSON or DataFrame) was requested last.

Saving and Loading Class Instances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

FinMesh uses ``Pickle`` to save and load states. It's a Python standard library and is perfect for the task.
When we 'pickle' something (like a cucumber or a class instance) we are preserving it for later.

Pickling is useful because every time you call a class method, you are using IEX Cloud credits.
To keep from having to make the same request over and over, we can save the class (and the information that has been assigned to a class attribute) for later.
Pickling is fairly straight forward. Let's say we create an instance of IEXStock for AAPL, and call the key stats method.
Then we will pickle the result to save it for later:

  >>> AAPL = IEXStock('AAPL')
  >>> AAPL.get_key_stats()
  # A whole bunch of JSON containing the keys and values from the Key Stats endpoint
  >>> AAPL.pickle_class_state()
  # Output a file with the pickled class inside.

In this example, assuming the date is January 27th, 2022, the output file would be called ``'AAPL_2022-01-27.pickle'``.
An internal method takes care of naming the file so that every one is predictable and standard.

In order to load a pickled class, we can call the ``unpickle_class_state(*file*)`` method, specifying the file name of the pickled state.

Using Base methods to Access Data
===================================

The IEXStock class is built on a collection of sub-modules containing simple methods that request and receive JSON.
These have no Pandas output and are purposefully minimum viable methods for accessing IEX Cloud data.

The base methods for IEX Cloud are contained in the ``stock``, ``premium``, ``market``, and ``forex`` modules.
You will need to specify which module you would like to access in the ``import`` path.
All the methods you need for stock specific data will be in the ``stock`` sub-module.
