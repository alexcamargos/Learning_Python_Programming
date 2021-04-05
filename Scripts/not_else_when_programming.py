#!/usr/bin/env python
# encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: not_else_when_programming.py
# Version: 0.0.1
#
# Summary: Don't Use Else When Programming.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""
Don't Use Else When Programming.

This may sound crazy but I really don't use the else keyword in my programming anymore.
When I do end up using else it usually leads to worse code than if I purposely avoided it.
In this video I explain exactly why that is.

"""


class Person:
    """Simple representation of a person."""

    def __init__(self, age=None):
        """Applying age."""
        self.age = age


def can_drink(person):
    """Checks if the person can drink by analyzing the age."""

    if person.age is not None:
        if person.age < 18:
            print('Nope! \U0001F476')
        elif person.age < 21:
            print('Not in the USA! \U0001F914')
        else:
            print('Yes! You can drink! \U0001F37A')
    else:
        print('You are not a person! \U0001F916')


def better_can_drink_response(age):

    if age < 18:
        return 'Nope! \U0001F476'

    if age < 21:
        return 'Not in the USA! \U0001F914'

    return 'Yes! You can drink! \U0001F37A'


def better_can_drink(person):
    """Checks if the person can drink by analyzing the age, don't use the else keyword."""

    if person.age is None:
        return print('You are not a person! \U0001F916')

    return print(better_can_drink_response(person.age))


def main():
    """Main function."""

    # Defining people.
    not_person = Person()
    person1 = Person(12)
    person2 = Person(19)
    person3 = Person(35)

    list_of_person = [not_person, person1, person2, person3]

    # Checking if the person can drink
    for person in list_of_person:
        print(f'Age: {person.age}', end=' ')
        # Using else keyword.
        can_drink(person)

    print()

    for person in list_of_person:
        print(f'Age: {person.age}', end=' ')
        # Not using else keyword.
        better_can_drink(person)


if __name__ == '__main__':
    # Running the script.
    main()
