#  #!/usr/bin/env python
#  encoding: utf-8

# Estamos criando uma string usando substituição.
x = 'There are %d types od peoples.' % 10
binary = 'binary'
do_not = "don't"
# Dupla substituição de strings.
y = 'Those who know %s and those who %s.' % (binary, do_not)

print(x)
print(y)

# Substituindo strings dentro da função print().
print('I said: %r.' % x)
print("I also said: '%s'." % y)

# hilarious = True
hilarious = False
joke_evaluation = "Isn't that joke so funny!? %r"

print(joke_evaluation % hilarious)

w = 'This is the left side of...'
e = 'a string with a right side.'

# Passando mais de uma variável para a função print(), separador padrão espaço em branco..
print(w, e)
