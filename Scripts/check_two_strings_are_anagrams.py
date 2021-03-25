#  #!/usr/bin/env python
#  encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: check_two_strings_are_anagrams.py
# Version: 1.0
#
# Summary: Find Whether Two Strings are Anagrams
#          An interesting application of the Counter class is to find anagrams.
#          An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
#          If the Counter objects of two strings are equal, then they are anagrams.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""
Find Whether Two Strings are Anagrams

An interesting application of the Counter class is to find anagrams.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
If the Counter objects of two strings are equal, then they are anagrams.
"""

# A Counter is a dict subclass for counting hashable objects.
from collections import Counter

string_1 = 'acbde'
string_2 = 'abced'
string_3 = 'abcda'
strings_list = [string_1, string_2, string_3]

my_list = [Counter(counter) for counter in strings_list]

if my_list[0] == my_list[1]:
    print(f'{string_1} and {string_2} are anagram.')
else:
    print(f"{string_1} and {string_2} aren't anagram.")

if my_list[1] == my_list[2]:
    print(f"{string_2} and {string_3} are anagram.")
else:
    print(f"{string_2} and {string_3} aren't anagram.")
