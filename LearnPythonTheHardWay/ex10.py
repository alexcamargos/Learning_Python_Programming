#  #!/usr/bin/env python
#  encoding: utf-8

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# My solution for:
# "Combine escape sequences and format strings to create a more complex format."
somethings_to_bay = ['Cat food', 'Fishies', 'Catnip', 'Grass']
print('\nI have to bay:')
for item in somethings_to_bay:
    print('\t* %s:' % item.upper())

escape_sequences = '''
Escape What it does.
\\ Backslash (\)
\' Single- quote (')
\" Double- quote (")
\a ASCII bell (BEL)
\b ASCII backspace (BS)
\f ASCII formfeed (FF)
\n ASCII linefeed (LF)
\r ASCII carriage return (CR)
\t ASCII horizontal tab (TAB)
\v ASCII vertical tab (VT)
\ooo Character with octal value oo
'''

# print(escape_sequences)

# # Fun piece of code.
# while True:
#     for i in ['/', '-', '|', '\\', '|']:
#         print('%s\r' % i)
