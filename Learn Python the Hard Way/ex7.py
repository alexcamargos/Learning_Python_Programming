#  #!/usr/bin/env python
#  encoding: utf-8

# Imprimi algumas informações na tela, utilizando propriedades de formatação de string.
print('Mary had a little lamb.')
# Formatação de strings aceita inclusive outras strings diretamente, não apenas variáveis.
print("It's fleece was white as %s." % 'snow')
# Multiplicação de string por inteiro (concatenação).
print('.' * 10)

# Atribuição de variáveis a strings.
end1 = 'C'
end2 = 'h'
end3 = 'e'
end4 = 'e'
end5 = 's'
end6 = 'e'
end7 = 'B'
end8 = 'u'
end9 = 'r'
end10 = 'g'
end11 = 'e'
end12 = 'r'

# Watch that comma at the end. Try removing it to see whats happens.
# Utilização dos argumentos SEP e END da função print().
print(end1, end2, end3, end4, end5, end6, sep='', end=' ')
print(end7, end8, end9, end10, end11, end12, sep='')
