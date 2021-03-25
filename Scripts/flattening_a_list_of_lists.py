#  #!/usr/bin/env python
#  encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: flattening_a_list_of_lists.py
# Version: 1.0
#
# Summary: Flattening a List of Lists
#          Sometimes you’re not sure about the nesting depth of your list,
#          and you simply want all the elements in a single flat list.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""
Flattening a List of Lists

Sometimes you’re not sure about the nesting depth of your list,
and you simply want all the elements in a single flat list.
"""

# if you only have one depth nested_list, use this:
flatten_one_depth = lambda my_list: [item for sublist in my_list for item in sublist]

my_list_01 = [[0, 1, 2], [3], [4, 5, 6], [7, 8], [9]]

print(flatten_one_depth(my_list_01))
