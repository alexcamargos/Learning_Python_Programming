#  #!/usr/bin/env python
#  encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: frequency_elements_list.py
# Version: 0.0.1
#
# Summary: Finding frequency of each element in a list.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""
Finding frequency of each element in a list

There are multiple ways of doing this, but my favorite is using the Python Counter class.

Python counter keeps track of the frequency of each element in the container.
Counter() returns a dictionary with elements as keys and frequency as values.

We also use the most_common() function to get the most_frequent element in the list.
"""


from collections import Counter

my_list = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e', 'e', 'e', 'e', 1, 1, 1, 2, 2, 3, 3, 3, 3]

# Defining a counter object.
my_count = Counter(my_list)

# Of all elements:
print(my_count)

# Of individual element:
print(f"Number of occurrences of C: {my_count['c']}")

# Most frequent element:
print(f'Most frequent element: {my_count.most_common(1)}')
