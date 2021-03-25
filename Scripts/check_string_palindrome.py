#  #!/usr/bin/env python
#  encoding: utf-8

#  --------------------------------------------------------------------------------------------------------------------
#
#  Name: check_string_palindrome.py
#  Version: 1.0
#  Summary: Check if a given string is a palindrome or not become a straightforward program in Python.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#
#  --------------------------------------------------------------------------------------------------------------------

"""Check if a given string is a palindrome or not become a straightforward program in Python."""


# A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as
# forward, such as madam or racecar. There are also numeric palindromes, including date/time stamps using
# short digits 11/11/11 11:11 and long digits 02/02/2020.Sentence-length palindromes ignore capitalization,
# punctuation, and word boundaries.

my_string_01 = 'abcba'
my_string_02 = '11/11/11'
my_string_03 = '02-02-2020'
my_string_04 = '123123'
my_string_05 = 'alexsander'

# Normalizing the data for use in the algorithm.
new_string_02 = ''.join(my_string_02.split('/'))
new_string_03 = ''.join(my_string_03.split('-'))

# May new data.
my_list = [my_string_01, new_string_02, new_string_03, my_string_04, my_string_05]

# Filtering palindrome string using list comprehension
# List comprehension provides us with an elegant way of creating lists based on other lists.
palindromes = [string for string in my_list if string == string[::-1]]

for string in palindromes:
    print(f'{string} is a palindrome.')
