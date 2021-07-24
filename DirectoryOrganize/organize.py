#!/usr/bin/env python
# encoding: utf-8

# ---------------------------------------------------------------------------
#
# Name: organize.py
# Version: 0.0.1
#
# Summary: Python project to facilitate organize of cluttered folder.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# ---------------------------------------------------------------------------

"""Python project to facilitate organize of cluttered folder."""

import os
from fnmatch import filter
from functools import partial
from itertools import chain
from shutil import move, Error

# The absolute path of the working directory where
# Python is currently running.
base_directory = os.getcwd()

# So for simplicity's sake, we will only the essential folders:
root_directories = ['Audios',
                    'Compressed',
                    'Ebooks',
                    'Executable',
                    'Images',
                    'PDFs',
                    'Scripts',
                    'Videos']

list_of_patterns = {
    # Let's be absolutely sure we're getting everything that
    # looks like audio files.
    'audio_files': ['*.aac',
                    '*.flac',
                    '*.m4a',
                    '*.mp3',
                    '*.msv',
                    '*.ogg',
                    '*.wav',
                    '*.wma'],
    # Let's be absolutely sure we're getting everything that
    # looks like compressed files.
    'compressed_files': ['*.7z',
                         '*.dmg',
                         '*.gz',
                         '*.iso',
                         '*.rar',
                         '*.rz',
                         '*.tar*',
                         '*.zip'],
    # Let's be absolutely sure we're getting everything that
    # looks like e-books files.
    'ebooks_file': ['*.azw*',
                    '*.epub',
                    '*.mobi'],
    # Let's be absolutely sure we're getting everything that
    # looks like executable files.
    'executable_files': ['*.exe'],
    # Let's be absolutely sure we're getting everything that
    # looks images files.
    'image_files': ['*.bpm',
                    '*.eps',
                    '*.gif',
                    '*.jpeg',
                    '*.jpg',
                    '*.png',
                    '*.raw',
                    '*.tif',
                    '*.tiff',
                    '*.webp'],
    # Let's be absolutely sure we're getting everything that
    # looks like PDFs files.
    'pdf_file': ['*.pdf'],
    # Let's be absolutely sure we're getting everything that
    # looks like scripts files.
    'scripts_file': ['*.bat',
                     '*.py',
                     '*.rb',
                     '*.sh'],
    # Let's be absolutely sure we're getting everything that
    # looks like video files.
    'video_files': ['*.avi',
                    '*.mov',
                    '*.mp2',
                    '*.mp4',
                    '*.mpeg',
                    '*.mpg',
                    '*.mpv',
                    '*.webm',
                    '*.wmv']
}


def make_directories_for_organize():
    """Create the root directories if they don't exist."""

    print("Create the root directories if they don't exist...")

    try:
        [os.mkdir(os.path.join(base_directory, directory)) for directory in
         root_directories if
         not os.path.exists(os.path.join(base_directory, directory))]
    except ValueError:
        raise ValueError('File directory may already exist.')


def list_files_by_patterns(directory, patterns):
    """Returns a generator yielding files matching the given patterns."""

    root_directory = directory or '.'
    patterns = patterns or ['*']

    if not os.path.exists(root_directory):
        raise ValueError(f'Directory not found {directory}')

    # List all files in the directory.
    with os.scandir(root_directory) as entry:
        file_list = [fname.name for fname in entry if fname.is_file()]

        filter_partial = partial(filter, file_list)

        for fname in chain(*map(filter_partial, patterns)):
            yield os.path.join(base_directory, fname)


def move_files_to_directory(fnames, destination, verbose=False):
    """Move the files to the corresponding directory."""

    for fname in fnames:
        if verbose:
            file = fname.split('\\')[-1]
            print(f"Moving {file} to {destination}.")

        try:
            move(fname, destination)
        except Error as error:
            print(f'Failure moving file from {fname} to {destination}.')
            print(error)


if __name__ == "__main__":
    make_directories_for_organize()

    # Create a generator of all image files in the current dir.
    print('Getting a list of all image files in the current directory...')
    image_files = list_files_by_patterns(base_directory,
                                         list_of_patterns['image_files'])
    move_files_to_directory(image_files,
                            os.path.join(base_directory, 'Images'),
                            verbose=True)
