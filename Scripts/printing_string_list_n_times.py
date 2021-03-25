#  #!/usr/bin/env python
#  encoding: utf-8

#  --------------------------------------------------------------------------------------------------------------------
#
#  Name: printing_string_list_n_times.py
#  Version: 1.0
#
#  Summary: You can use multiplication (*) with strings or lists.
#           This allows us to multiply them as many times as we like.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------

"""You can use multiplication (*) with strings or lists. This allows us to multiply them as many times as we like."""

# Number of repetitions:
n = 3

my_string = "abc"
my_list_01 = [1, 2, 3]
my_list_02 = ['*']

print(my_string * n)

print(my_list_01 * n)

# Define a list with a constant value.
print(my_list_02 * n)
