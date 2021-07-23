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

base_directory = r'D:\WORKSPACE\Python\LearningPython' \
                 r'Programming\DirectoryOrganize\tmp'

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
                        '*.ogg',
                        '*.wav']

# Let's be absolutely sure we're getting everything that
# looks like compressed files.
compressed_files_patterns = ['*.7z',
                             '*.rar',
                             '*.tar*',
                             '*.zip']

# Let's be absolutely sure we're getting everything that
# looks like e-books files.
ebooks_file_patterns = ['*.azw*',
                        '*.epub',
                        '*.mobi']

# Let's be absolutely sure we're getting everything that
# looks like executable files.
executable_files_patterns = ['*.exe']

# Let's be absolutely sure we're getting everything that
# looks images files.
image_files_patterns = ['*.bpm',
                        '*.eps',
                        '*.gif',
                        '*.jpeg',
                        '*.jpg',
                        '*.png',
                        '*.raw',
                        '*.tif',
                        '*.tiff']

# Let's be absolutely sure we're getting everything that
# looks like PDFs files.
pdf_file_patterns = ['*.pdf']

# Let's be absolutely sure we're getting everything that
# looks like scripts files.
scripts_file_patterns = ['*.bat',
                         '*.py',
                         '*.rb',
                         '*.sh']

# Let's be absolutely sure we're getting everything that
# looks like video files.
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

    [os.mkdir(base_directory + '/' + directory) for directory in
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


if __name__ == "__main__":
    make_directories_for_organize()

    # create a generator of all jpg files in the current dir.
    print("Getting a list of all jpg files in the current dir...")

    image_files = list_files_by_patterns(base_directory, image_files_patterns)

    for file in image_files:
        print(file)
