Installation
############

Install FinMesh using pip for a tested, up-to-date version::

  pip install FinMesh

Dependencies and Module-Specific Requirements
=============================================

Depending on your use-case, there may be dependencies that are required for complete functionality.
If you are only interested in accessing IEX Cloud, ``pandas`` will be the only required install.
Below is a list of non-standard packages that are required and the modules that require them:

- Pandas [iex] ``pip install pandas``

- xmltodict [usgov] ``pip install xmltodict``

- Beautiful Soup [edgar] ``pip install bs4``

- Natural Language Toolkit [edgar] ``pip install nltk``


API Token Setup
===============

Some APIs require authentication through the use of tokens.
These tokens should be set up as environment variables in the bash profile.
A great article on how to do this on Mac is available here:

`My Mac OSX Bash Profile <https://natelandau.com/my-mac-osx-bash_profile/>`_

Or you can follow the guide down below for Mac and Linux.

Click `HERE <https://iexcloud.io/>`_ for your free IEX token.
This token must be stored as IEX_TOKEN in your environment variables.

Click `HERE <https://fred.stlouisfed.org/>`_ for your free FRED token.
This token must be stored as FRED_TOKEN in your environment variables.

What is an Environment Variable?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Environment variables are used in FinMesh to store API tokens and token-related data.
Tokens are like passwords that API providers use to authenticate the requests being made.
This ensures that (1) unauthorized parties cannot access the data or spam the API with bogus requests (such as in DDOS attacks) and (2) users can track their useage and manage permissions.
The IEX Cloud and FRED APIs both use tokens to authenticate users, and IEX in particular uses tokens to track useage and manage the level of services available.

In these examples we will be setting global environment variables using the standard bash profiles available on both MacOS and Linux.
You'll want to fire up a terminal window now so you can follow along.

For Mac users, your bash profile is called ``.bash_profile``, pretty simple.
When you open this, you'll likely find an empty file.

For Linux users, your bash profile is called ``.bashrc``.
Depending on your distribution, you may or may not find some pre-made bash shortcuts and other assorted code inside, we don't need to worry about any of that right now.

Your bash profile is stored in the User's home directory, this is the directory that a new terminal window will automatically open into so if you have just opened a new window, you're in the right place! This directory is most commonly denoted with a '~' before a '$'. If you have navigated into a folder, simply type 'cd' to return to the home directory. Now that you are in the correct directory lets open your bash profile using nano. Nano is simply a text editor that is built into terminal. Type this and then hit enter, and you'll be taken to your bash profile.

Mac::

  nano .bash_profile

Linux::
  
  nano .bashrc

Setting Up Your Token Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you are ready to add some token variables, you can go ahead and collect them from IEX and/or FRED from the links at the beginning of this page.

In the standard ``IEX_TOKEN`` variable, you'll want to paste your PUBLIC token from IEX.
This way if you accidentally publish this code, or otherwise have the token compromised you can simply cut that token off from API privileges.
You can of course use the secret key, but you are setting yourself up for a security vulnerability.

The ``IEX_SANDBOX_TOKEN`` is also fairly self-explanatory.
You can find this by switching to 'Sandbox Mode' in the IEX Console and looking where your regular tokens would normally be.

The ``SANDBOX`` boolean variable will tell FinMesh whether you want to access Sandbox data instead of the real data.
This is really useful when you are testing code and don't want to use credits.

The ``FRED`` token is even more straight forward.
There are no sandbox options and no public/private versions of keys.
Simply paste in your token and you are good to go!

Once you've written out the code below and filled in the blanks with the appropriate tokens, your bash profile is all set::

  # FinMesh Token Setup

  # Public IEX Cloud Token
  IEX_TOKEN=#PLACE-YOUR-TOKEN-HERE#
  # Sandbox IEX Token
  IEX_SANDBOX_TOKEN=#PLACE-YOUR-TOKEN-HERE#
  # Sandbox State
  SANBOX=False
  # FRED Token
  FRED_TOKEN=#PLACE-YOUR-TOKEN-HERE#

You can now exit nano by hitting ``CTRL+O`` to writeout(save) your work and then ``CTRL+X`` to close the nano editor.
Once you are back into the terminal, type the following to apply the changes to your environment.

Mac:
  ``source .bash_profile``

Linux:
  ``source .bashrc``

Conclusion
^^^^^^^^^^

You are now all set up to use FinMesh! If you have questions or concerns you are always free to reach out to me at the links below! In the future this type of setup may not be neccesary as we look at other ways to supply tokens that retains the security and seamlessness of this method while being easier to configure.
