#  #!/usr/bin/env python
#  encoding: utf-8

from sys import argv

# script, first, second, third = argv

script, age, height = argv

weight = input('How much do you weigh? ')

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))

# print('The script is called: ', script)
# print('Your first variable is: ', first)
# print('Your second variable is: ', second)
# print('You third variable is: ', third)
