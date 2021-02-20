#!/usr/bin/env python
#  encoding: utf-8
#
#  --------------------------------------------------------------------------------------------------------------------
#  Name: pdf_brute_force_decrypt.py
#  Version: 0.1
#  Summary: Brute-Force PDF Password Breaker - A program that will decrypt the PDF by trying every possible
#  Portuguese word until it finds one that works.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  --------------------------------------------------------------------------------------------------------------------
#
# O arquivo contendo o dicionário foi obtido aqui do projeto Dicionário br.ispell
# copyright Ricardo Ueda Karpischek (ueda@ime.usp.br) - http://www.ime.usp.br/~ueda/br.ispell/
#
#  --------------------------------------------------------------------------------------------------------------------

"""Brute-Force PDF Password Breaker - A program that will decrypt the PDF by trying every possible Portuguese word
until it finds one that works, this is called a brute force password attack.

Educational implementation only.
"""

from os import path
from time import time

import PyPDF2 as pypdf

# Some useful variables.
this_folder = path.dirname(path.abspath(__file__))
dictionary_file = path.join(this_folder, 'dictionary.txt')
# Simple password with a single word in Portuguese without accents.
pdf_file = path.join(this_folder, 'encrypted_file.pdf')
# pdf_file = path.join(this_folder, 'encrypted_file_2.pdf')


def load_password_list(dictionary):
    """Loads the contents of the dictionary file into memory, returning a list of all the words in the file."""

    with open(dictionary) as _file:
        return [word.strip() for word in _file.readlines()]


def main():
    # Load the file containing the dictionary.
    password_list = load_password_list(dictionary_file)
    # Open the encrypted PDF file.
    my_pdf_file_encrypted = pypdf.PdfFileReader(open(pdf_file, 'rb'))

    password_try = 0

    # Try to decrypt the PDF file.
    if not my_pdf_file_encrypted.isEncrypted:
        print('This file is not encrypted. You can successfully open it.')
    else:
        print('The file is encrypted, trying decryption...')
        stat_time = time()

        # Iterate over password list.
        for word in password_list:
            password_try += 1

            # Checking upper case.
            if my_pdf_file_encrypted.decrypt(word.upper()):
                print(f'Decrypted file, to open use this password: {word.upper()}')
                break

            # Checking lower case.
            if my_pdf_file_encrypted.decrypt(word.lower()):
                print(f'Decrypted file, to open use this password: {word.lower()}')
                break

        end_time = time()
        print(f'Runtime: {end_time - stat_time}')
        print(f'Number of attempts: {password_try}')


if __name__ == '__main__':
    main()
