#!/usr/bin/env python
# encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: descriptors_at_run_time.py
# Version: 1.0
#
# Summary: Criando atributos de propriedade no tempo de execução.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""Criando atributos de propriedade no tempo de execução."""


class Person:
    """The base class of person."""

    def __set_property(self, attribute, value):
        """Sets the named attribute on the given object to the specified value."""

        setattr(self, attribute, value.lower())

    def __get_property(self, attribute):
        """Get a named attribute from an object."""

        return getattr(self, attribute)

    def add_property(self, attribute):

        # Create local setter and getter with a particular attribute name.
        __getter = lambda self: self.__get_property(attribute)
        __setter = lambda self, value: self.__set_property(attribute, value)

        # Construct property attribute and add it to the class.
        setattr(self, attribute, property(fget=__getter,
                                          fset=__setter,
                                          doc='Auto‑generated method.'))


user = Person()
user.add_property('username')
user.add_property('password')

user.username = 'alcamargos'
user.password = '123456'

print(user.__dict__)

print(f'Username: {user.username}')
print(f'Password: {user.password}')
