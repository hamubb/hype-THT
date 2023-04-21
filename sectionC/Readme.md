## check_isbn - A command-line tool to validate ISBN10 and ISBN13 numbers
To run check_isbn all you need is a python preferebly python3.9. After installing 
python you can go ahead and create a virtual environment and then install the only 
requirement which is Pytest.


***How to get started on Linux***

check_isbn needs pytest to run the tests includeded with this module.

First create a virtual environment 

$ virtualenv venv
$ . venv/bin/activate

pip install pytest


***How to use it***

To run the programm make sure you are in the directory where check_isbn.py is located. And then
run the following at:

$ python -m check_isbn.py

Respond by entering an ISBN number without spaces or dashes for example: 4376765543674


***Testing***

To run the tests simply run:

$ pytest -s tests.py

***Resources***

For valid ISBN numbers please visit [This link](https://www.topshelfcomix.com/catalog/isbn-list)
