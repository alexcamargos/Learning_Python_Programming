#  #!/usr/bin/env python
#  encoding: utf-8

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

_hash_algorithm_map = {
    # 'adler32': zlib.adler32,
    # 'crc32': zlib.crc32,
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,
    'sha3_256': hashlib.sha3_256,
    'sha3_512': hashlib.sha3_512,
}

SUPPORTED_ALGORITHMS = set(_hash_algorithm_map.keys())


class FileHash:

    def __init__(self, hash_algorithm='sha512', chunk_size=65536):
        """"Initialize the class."""

        if hash_algorithm not in SUPPORTED_ALGORITHMS:
            raise ValueError(f'Error, unsupported hash/checksum algorithm: {hash_algorithm}')

        self.hash_algorithm = hash_algorithm
        self.chunk_size = chunk_size

    def generate_file_hash(self, file_name):
        """Generate the hash of a file."""

        file_hash = _hash_algorithm_map[self.hash_algorithm]()

        try:
            with open(file_name, mode='rb', buffering=0) as fname:
                file_block = fname.read(self.chunk_size)

                while file_block:
                    file_hash.update(file_block)
                    file_block = fname.read(self.chunk_size)

        # System-related error, including I/O failures.
        except OSError as error:
            print(f'I/O error({error.errno}): {error.strerror}')

            return None

        return file_hash.hexdigest()


hash_file = FileHash()
print(hash_file.generate_file_hash(r'D:\_Teste_FileFinder\rufus-3.9p.exe'))
