#  #!/usr/bin/env python
#  encoding: utf-8

#  --------------------------------------------------------------------------------------------------------------------
#
#  Name: finding_unique_elements_string.py
#  Version: 1.0
#
#  Summary: Finding unique elements in a string using python set.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------

"""Finding unique elements in a string using python set."""


string_01 = "aabbbccccdddddeeeeee"
string_02 = "ffggghhhhjjjjjkkkkkk"
string_03 = "aaeeeiiiiooooouuuuuu"
string_04 = "zzzaaaxxxeeevvviii"
string_05 = "1122333444455555666666"
string_06 = "123321456654789987"

my_strings = [string_01, string_02, string_03, string_04, string_05, string_06]

for _str in my_strings:
    # Converting the string to a python set.
    temp_string = set(_str)

    # Stitching back set into a string using .join().
    string = ''.join(sorted(temp_string))

    print(f"Unique elements present in the string '{_str}': {string}")
