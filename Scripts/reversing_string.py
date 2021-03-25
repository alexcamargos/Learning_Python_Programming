#  #!/usr/bin/env python
#  encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: reversing_string.py
# Version: 1.0
#
# Summary: The following snippet reverses a string using the Python slicing operation.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""The following snippet reverses a string using the Python slicing operation."""

string_01 = 'abcdef'
string_02 = '123456'
string_03 = '123456789'
string_04 = 'abcdefghijl'

my_string = [string_01, string_02, string_03, string_04]

for _str in my_string:
    # Reversing a string using python slicing.
    new_string = _str[::-1]

    print(f"Reversing a string the string '{_str}': {new_string}")
