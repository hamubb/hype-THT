## check_isbn - A command-line tool to validate ISBN10 and ISBN13 numbers
To run check_isbn all you need is a python preferebly python3.9. After installing 
python you can go ahead and create a virtual environment and then install the only 
requirement which is Pytest.


***How to get started on Linux and MacOs***

check_isbn needs pytest to run the tests includeded with this module.

First create a virtual environment 
```
$ virtualenv venv
$ . venv/bin/activate
```

```bash
pip install pytest
```

***How to get started on Microsoft Windows***


Install Python

To install Python on your machine go to https://www.python.org/downloads/. The
website should offer you a download button for the latest Python version.
Download the executable installer and run it. Check the boxes next to "Install
launcher for all users (recommended)" then click "Install Now".

After installation, open the command prompt and check that the Python version
matches the version you installed by executing::

    ...\> py --version


***About ``pip``***


`pip`_ is a package manager for Python and is included by default with the
Python installer. It helps to install and uninstall Python packages
(such as Pytest!). For the rest of the installation, we'll use ``pip`` to
install Pytest packages from the command line.

.. _pip: https://pypi.org/project/pip/

.. _virtualenvironment:


***Setting up a virtual environment***


Python comes with `venv` for managing virtual environments


To create a virtual environment for our project, open a new command prompt,
navigate to the sectionC folder and then enter the
following::

    ...\> py -m venv isbn

This will create a folder called 'isbn' and set up the virtual environment. To activate the environment, run::

    ...\> isbn\Scripts\activate.bat

The virtual environment will be activated and you'll see "(isbn)" next
to the command prompt to designate that. Each time you start a new command
prompt, you'll need to activate the environment again.

Pytest can be installed easily using ``pip`` within your virtual environment.

In the command prompt, ensure your virtual environment is active, and execute
the following command::

    ...\> py -m pip install pytest

This will download and install the Pytest which is the only dependency for this project


***How to use it***

To run the programm make sure you are in the directory where check_isbn.py is located. And then
run the following at:

```
$ python -m check_isbn
```

Respond by entering an ISBN number without spaces or dashes for example: 4376765543674


***Testing***

To run the tests simply run:
```bash
$ pytest -s tests.py
```

When prompted for an ISBN number hit Enter/Return. The tests will run and results will be displayed.

***Resources***

For valid ISBN numbers please visit [This link](https://www.topshelfcomix.com/catalog/isbn-list)
