#  #!/usr/bin/env python
#  encoding: utf-8

#  --------------------------------------------------------------------------------------------------------------------
#
#  Name: combining_list_strings_using_string_join_method.py
#  Version: 1.0
#  Summary: The .join() method combines a list of strings passed as an argument into a single string.
#           In our case, we separate them using the comma separator.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------

"""
The join() method combines a list of strings passed as an argument into a single string.
In our case, we separate them using the comma separator.
"""


my_tuple = ('My', 'name', 'is', 'Alexsander', 'Lopes', 'Camargos.')
my_list = ['My', 'name', 'is', 'Alexsander', 'Lopes', 'Camargos.']
my_dic = {1: 'My', 2: 'name', 3: 'is', 4: 'Alexsander', 5: 'Lopes', 6: 'Camargos.'}

# Separator is whitespace character.
my_separator = ' '

# Join all items in a tuple into a string, using a whitespace character as separator:
str_tuple = my_separator.join(my_tuple)

# Join all items in a list into a string, using a whitespace character as separator:
str_list = my_separator.join(my_list)

# Join all items in a dictionary into a string, using a whitespace character as separator:
str_dic = my_separator.join(my_dic.values())

print(f'Tuple: {str_tuple}')
print(f'List: {str_list}')
print(f'Dictionary: {str_dic}')
