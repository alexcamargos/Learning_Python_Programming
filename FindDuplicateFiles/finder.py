#!/usr/bin/env python
# encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: finder.py
# Version: 0.0.1
#
# Summary: The File Finder allows you to track duplicate files in a specific directory,
#          allowing free up storage space. You can tell the File Browser exactly what to
#          look for and what to ignore and delete duplicate files easily.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""
Finding Duplicate Files

The File Finder allows you to track duplicate files in a specific directory, allowing free up storage space.
You can tell the File Browser exactly what to look for and what to ignore and delete duplicate files easily.
"""

import stat
import sys

from hashlib import sha256
from pathlib import Path

_BUFFER_SIZE = 1024 * 8


def _signature(st):
    return stat.S_IFMT(st.st_mode), st.st_size, st.st_mtime


class File:
    def __init__(self, path, buffer_size=_BUFFER_SIZE):
        self.__path = path
        self.__file_hash = None
        self.__buffer_size = buffer_size
        self.signature = _signature(self.path.stat())

        self.generate_file_hash()

    def __repr__(self):
        """ Return repr(self). """

        print(f'{self.__class__.__name__}, File: {self.path.name}, Hash: {self.hash}')

    __str__ = __repr__

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value

    @property
    def hash(self):
        return self.__file_hash

    @hash.setter
    def hash(self, value):
        self.__file_hash = value

    def generate_file_hash(self):
        """Generate a SHA-256 hash for each file."""

        if not self.path:
            return False

        file_hash = sha256()
        try:
            with open(self.path, 'rb') as fname:
                file_block = fname.read(self.__buffer_size)

                while file_block:
                    file_hash.update(file_block)
                    file_block = fname.read(self.__buffer_size)

            self.hash = file_hash.hexdigest()
        # System-related error, including I/O failures.
        except OSError as error:
            self.hash = None
            print(f'I/O error({error.errno}): {error.strerror}')


class FileFinder:
    """The File Finder allows you to track duplicate files in a specific directory."""

    def __init__(self, directory):
        self.__directory = Path(directory)

    @property
    def directory(self):
        return self.__directory

    def exec(self):
        return [File(file) for file in self.list_all_files()]

    def list_all_files(self):
        """Iterate over the files in this directory."""

        return [file for file in self.directory.glob('**/*') if file.is_file()]


def filter_duplicate(file_list, shallow=False):
    """Finding duplicate files."""

    # TODO: Just check stat signature (do not read the files).
    if shallow:
        return

    unique_files = []
    duplicate_files = []
    unique_hash = []

    for file in file_list:
        if file.hash not in unique_hash:
            unique_hash.append(file.hash)
            unique_files.append(file)
        else:
            duplicate_files.append(file)

    return unique_files, duplicate_files


def main(output=sys.stdout):
    """Finding Duplicate Files main function."""

    directory = r'D:\_Teste_FileFinder'

    print(f'Finding Duplicate Files in {directory}\n', file=output)

    finder = FileFinder(directory)
    files = finder.exec()

    unique_files, duplicate_files = filter_duplicate(files)

    print(f'Unique files in {directory}:', file=output)
    for unique_file in unique_files:
        print(f'{unique_file.path}, HASH: {unique_file.hash}', file=output)

    print(f'\n\nDuplicate files in {directory}:', file=output)
    for duplicate_file in duplicate_files:
        print(f'{duplicate_file.path}, HASH: {duplicate_file.hash}', file=output)


if __name__ == '__main__':
    main()
