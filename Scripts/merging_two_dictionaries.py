#  #!/usr/bin/env python
#  encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: merging_two_dictionaries.py
# Version: 1.0
#
# Summary: Merging two dictionaries.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""
Merging Two Dictionaries

While in Python 2, we used the update() method to merge two dictionaries;
Python 3 made the process even simpler. In the script given below, two dictionaries are merged.

Values from the second dictionary are used in case of intersections.
"""


dict_1 = {'apple': 9, 'banana': 6, 'avocado': 6}
dict_2 = {'banana': 4, 'orange': 8, 'pear': 8}

combined_dict = {**dict_1, **dict_2}

print(combined_dict)
