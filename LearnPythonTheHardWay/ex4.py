#  #!/usr/bin/env python
#  encoding: utf-8

# Definimos a quantidade de carros disponíveis.
cars = 100
# Definimos quantos passageiros cada carro pode transportar.
space_in_a_car = 4
# Definimos quantos motorista temos disponíveis.
drivers = 30
# Definimos quantos passageiros precisam ser transportados.
passengers = 90
# Definimos quantos carros não tem um motorista a disposição.
cars_not_driven = cars - drivers
# Criamos a variável cars_driven apontando para o espaço de memoria que esta a variável drivers.
cars_driven = drivers
# Definimos qual a capacidade máxima de passageiros podemos transportar com os motoristas disponíveis.
carpool_capacity = cars_driven * space_in_a_car
# Definimos quantos passageiros precisamos levar em cada carro que tem motorista disponível para que possamos
# transportar todos.
average_passengers_per_car = passengers / cars_driven

print(f'There are {cars} cars available.')
print(f'There are only {drivers} drivers available.')
print(f'There will be {cars_not_driven} empty cars today.')
print(f'We can transport {carpool_capacity} people today.')
print(f'We have {passengers} to carpool today.')
print(f'We need to put about {average_passengers_per_car} in ech car.')
