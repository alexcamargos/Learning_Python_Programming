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
from collections import namedtuple
from pathlib import Path


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

FileHashResult = namedtuple('FileHashResult', ['file_name', 'hash'])


class FileHash:
    """Wrapping the hashlib module to facilitate calculating file hashes."""

    def __init__(self, hash_algorithm='sha512', chunk_size=65536):
        """"Initialize the class."""

        if hash_algorithm not in SUPPORTED_ALGORITHMS:
            raise ValueError(f'Error, unsupported hash/checksum algorithm: {hash_algorithm}')

        # The hash algorithm to use.
        self.hash_algorithm = hash_algorithm

        # The chunk size (in bytes) when reading files.
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

    def generate_files_hash(self, file_names):
        """Generate the hash of of multiple files."""

        return [FileHashResult(fname, self.generate_file_hash(fname)) for fname in file_names]

    def generate_directory_hash(self, directory_path, pattern=None):
        """Generate the hash of files in a directory."""

        if not pattern:
            pattern = '*'

        files_names = [file for file in directory_path.glob(pattern) if file.is_file()]

        hash_files = self.generate_files_hash(files_names)

        return hash_files


hash_file = FileHash()
print('generate_file_hash()')
print(hash_file.generate_file_hash(r'D:\_Teste_FileFinder\rufus-3.9p.exe'))


path = Path(r'D:\_Teste_FileFinder')
print('generate_directory_hash()')
for k in hash_file.generate_directory_hash(path):
    print(k.file_name, k.hash)

files = [r'D:\_Teste_FileFinder\README.md', r'D:\_Teste_FileFinder\cpython.png']
print('generate_files_hash()')
for i in hash_file.generate_files_hash(files):
    print(i.file_name, i.hash)
