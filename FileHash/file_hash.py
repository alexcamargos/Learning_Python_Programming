#!/usr/bin/env python
# encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: file_hash.py
# Version: 0.0.1
#
# Summary: Python project to facilitate the generation of hash/checksum for files and directorys.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""Python project to facilitate the generation of hash/checksum for files and directorys."""


import hashlib

from collections import namedtuple
from pathlib import Path


_HASH_ALGORITHM_MAP = {
    # 'adler32': zlib.adler32,
    # 'crc32': zlib.crc32,
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,
    'sha3_256': hashlib.sha3_256,
    'sha3_512': hashlib.sha3_512,
}

_SUPPORTED_ALGORITHMS = set(_HASH_ALGORITHM_MAP.keys())

_FileHashResult = namedtuple('FileHashResult', ['file_name', 'hash'])
_VerifyHashResult = namedtuple('VerifyHashResult', ['file_name', 'hashes_match'])


class FileHash:
    """Wrapping the hashlib module to facilitate calculating file hashes."""

    def __init__(self, hash_algorithm='sha512', chunk_size=65536):
        """"Initialize the class.

        chunk_size - Lets read stuff in 64 kb chunks."""

        if hash_algorithm not in _SUPPORTED_ALGORITHMS:
            raise ValueError(f'Error, unsupported hash/checksum algorithm: {hash_algorithm}')

        # The hash algorithm to use.
        self._hash_algorithm = hash_algorithm

        # The chunk size (in bytes) when reading files.
        self._chunk_size = chunk_size

    def generate_file_hash(self, file_name):
        """Generate the hash of a file."""

        # Automatically initializing the hash algorithm.
        file_hash = _HASH_ALGORITHM_MAP[self._hash_algorithm]()

        try:
            with open(file_name, mode='rb', buffering=0) as fname:
                fblock = fname.read(self._chunk_size)

                while fblock:
                    file_hash.update(fblock)
                    fblock = fname.read(self._chunk_size)

        # System-related error, including I/O failures.
        except OSError as error:
            print(f'I/O error({error.errno}): {error.strerror}')

            return None

        return file_hash.hexdigest()

    def generate_files_hash(self, file_names):
        """Generate the hash of of multiple files."""

        return [_FileHashResult(fname, self.generate_file_hash(fname)) for fname in file_names]

    def generate_directory_hash(self, directory_path, pattern=None):
        """Generate the hash of files in a directory."""

        if not pattern:
            pattern = '*'

        files_names = [file for file in directory_path.glob(pattern) if file.is_file()]

        hash_files = self.generate_files_hash(files_names)

        return hash_files

    def verify_checksum(self, checksum_file_name):
        """Verifying the checksums of a file or set of files.

        The checksum file is a text file where each line has the hash and filename in the following format:
            ChecksumHash[SPACE][ASTERISK]FileName
        """

        hashes_match = []

        with open(checksum_file_name, mode='r') as checksum_list:
            for file_line in checksum_list:
                expected_hash, file_name = file_line.strip().split(" ", 1)

                if file_name.startswith('*'):
                    file_name = file_name[1:]

                actual_hash = self.generate_file_hash(file_name)
                hashes_match.append(_VerifyHashResult(file_name, expected_hash == actual_hash))

        return hashes_match


hash_file = FileHash()
print(hash_file.generate_file_hash(r'D:\Videos\Filmes\The.Matrix.1999.2160p.UHD.BluRay.X265-IAMABLE\The.Matrix.1999.2160p.UHD.BluRay.X265-IAMABLE.mkv'))

# print('generate_file_hash()')
# print(hash_file.generate_file_hash(r'D:\_Teste_FileFinder\rufus-3.9p.exe'))
#
# path = Path(r'D:\_Teste_FileFinder')
# print('generate_directory_hash()')
# for k in hash_file.generate_directory_hash(path):
#     print(k.file_name, k.hash)
#
# files = [r'D:\_Teste_FileFinder\README.md', r'D:\_Teste_FileFinder\cpython.png']
# print('generate_files_hash()')
# for i in hash_file.generate_files_hash(files):
#     print(i.file_name, i.hash)
#
# for x in hash_file.verify_checksum(r'D:\_Teste_FileFinder\sha512sum.txt'):
#     print(x.file_name, x.hashes_match)
