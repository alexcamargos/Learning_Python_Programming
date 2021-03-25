#!/usr/bin/env python
# encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: file_name.py
# Version: 0.0.1
#
# Summary: Time Taken to Execute a Piece of Code.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""The following snippet uses the time library to calculate the time taken to execute a piece of code."""

import time


class TimeControl:
    def __init__(self):
        self.__start_time = 0
        self.__end_time = 0

    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value

    @property
    def time_spent(self):
        return round(((self.end_time - self.start_time) * 1000), 2)


flatten_one_depth = lambda _list: [item for sublist in _list for item in sublist]

my_list = [[0, 1, 2], [3], [4, 5, 6], [7, 8], [9]] * 10000

time_flatten = TimeControl()
time_flatten.start_time = time.time()
flatten_list = flatten_one_depth(my_list)
time_flatten.end_time = time.time()

print(f'Time spent to flattening a list of lists: {time_flatten.time_spent} ms')
