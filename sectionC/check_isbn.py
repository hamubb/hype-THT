#!/usr/bin/python

isbn_string = input("Please Enter a valid ISBN number:\n")


ISBN_MULTIPLIERS = "1313131313131"


def validate_isbn_number(isbn_string):
    """Checks a supplied isbn number, if the number is invalid, prints out:
    'Invalid',If the supplied number is valid, it prints out 'Valid'.
    ISBN10 numbers are converted to ISBN13 numbers and the new isbn number
    is printed in ISBN13 format
    """
    isbn_string = isbn_string.replace("_", "").replace(" ", "").replace("-", "")
    result = 0

    if len(isbn_string) != 10:
        if len(isbn_string) != 13:
            if not isbn_string[0:9].isdigit():
                return 'Invalid'

    if len(isbn_string) == 13:
        zipped = list(zip(isbn_string, ISBN_MULTIPLIERS))
        result += sum([int(x) * int(y) for x, y in zipped])

        if result % 10 == 0:
            return 'Valid'
        else:
            return 'Invalid'

    if len(isbn_string) == 10:
        zipped = list(zip(reversed(range(2, 11)), isbn_string))
        result += sum([int(x) * int(y) for x, y in zipped])

        if isbn_string[9].lower() == 'x':
            result += 10
        else:
            result += int(isbn_string[9])
        if result % 11 == 0:
            isbn_string = '978' + isbn_string[:-1]

            zipped = list(zip(isbn_string, ISBN_MULTIPLIERS))
            result = sum([int(x) * int(y) for x, y in zipped])

            if result % 10 == 0:
                isbn_string = isbn_string + '0'
            else:
                isbn_string = isbn_string + str(10 - (result % 10))
            return isbn_string
        else:
            return 'Invalid'


print(validate_isbn_number(isbn_string))
