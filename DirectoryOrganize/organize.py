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
from shutil import move

# base_directory = r'D:\WORKSPACE\Python\LearningPython' \
#                  r'Programming\DirectoryOrganize\tmp'

base_directory = '.'

# So for simplicity's sake, we will only the essential folders:
root_directories = ['Audios',
                    'Compressed',
                    'Ebooks',
                    'Executable',
                    'Images',
                    'PDFs',
                    'Scripts',
                    'Videos']

# Let's be absolutely sure we're getting everything that
# looks like audio files.
audio_files_patterns = ['*.aac',
                        '*.flac',
                        '*.m4a',
                        '*.mp3',
                        '*.msv',
                        '*.ogg',
                        '*.wav',
                        '*.wma']

list_of_patterns = {
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

compressed_files_patterns = ['*.7z',
                             '*.dmg',
                             '*.gz',
                             '*.iso',
                             '*.rar',
                             '*.rz',
                             '*.tar*',
                             '*.zip']
ebooks_file_patterns = ['*.azw*',
                        '*.epub',
                        '*.mobi']
executable_files_patterns = ['*.exe']
image_files_patterns = ['*.bpm',
                        '*.eps',
                        '*.gif',
                        '*.jpeg',
                        '*.jpg',
                        '*.png',
                        '*.raw',
                        '*.tif',
                        '*.tiff',
                        '*.webp']
pdf_file_patterns = ['*.pdf']
scripts_file_patterns = ['*.bat',
                         '*.py',
                         '*.rb',
                         '*.sh']
video_files_patterns = ['*.avi',
                        '*.mov',
                        '*.mp2',
                        '*.mp4',
                        '*.mpeg',
                        '*.mpg',
                        '*.mpv',
                        '*.webm',
                        '*.wmv']


def make_directories_for_organize():
    """Create the root directories if they don't exist."""

    print("Create the root directories if they don't exist...")

    [os.mkdir(base_directory + '\\' + directory) for directory in
     root_directories if not os.path.exists(base_directory + '/' + directory)]


def list_files_by_patterns(directory, patterns):
    """Returns a generator yielding files matching the given patterns."""

    root_directory = directory or '.'
    patterns = patterns or ['*']

    if not os.path.exists(root_directory):
        raise ValueError(f'Directory not found {directory}')

    # List all files in the root_directory.
    for root, dnames, fnames in os.walk(root_directory):
        filter_partial = partial(filter, fnames)

        for fname in chain(*map(filter_partial, patterns)):
            yield os.path.join(root, fname)


def move_files_to_directory(fnames, destination, verbose=False):
    """Move the files to the corresponding directory."""

    for fname in fnames:
        if verbose:
            file = fname.split('\\')[-1]
            print(f"Moving {file} to {destination}.")

        try:
            move(fname, destination)
        # TODO: Don't use bare 'except'
        except:
            return None


# Parse command line arguments.
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Organize files.')

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose mode.')

if __name__ == "__main__":
    make_directories_for_organize()

    # Create a generator of all image files in the current dir.
    print('Getting a list of all image files in the current directory...')

    image_files = list_files_by_patterns(base_directory,
                                         list_of_patterns['image_files'])

    move_files_to_directory(image_files,
                            base_directory + r'\Images',
                            verbose=True)
