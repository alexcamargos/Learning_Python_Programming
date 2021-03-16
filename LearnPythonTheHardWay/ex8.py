#  #!/usr/bin/env python
#  encoding: utf-8

# Variáveis que esta presente no código do exercício do livro.
formatter = '%r %r %r %r'
# Meus teste.
formatter2 = '%s %s %s %s'
print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter2 % ('one', 'two', 'three', 'four'))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ('I had this thing.',
                   'That you could type up right.',
                   "But it didn't sing.",
                   'So I said goodnight.'))
print(formatter2 % ('I had this thing.',
                    'That you could type up right.',
                    "But it didn't sing.",
                    'So I said goodnight.'))
