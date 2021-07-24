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


def audios_handling(verbose=True):
    """Handling of all audios files."""

    audios_files = list_files_by_patterns(base_directory,
                                          list_of_patterns['audio_files'])

    move_files_to_directory(audios_files,
                            os.path.join(base_directory, 'Audios'),
                            verbose)


def compressed_handling(verbose=True):
    """Handling of all compressed files."""

    compressed_files = list_files_by_patterns(base_directory,
                                              list_of_patterns[
                                                  'compressed_files'])

    move_files_to_directory(compressed_files,
                            os.path.join(base_directory, 'Compressed'),
                            verbose)


def ebooks_handling(verbose=True):
    """Handling of all ebooks files."""

    ebooks_files = list_files_by_patterns(base_directory,
                                          list_of_patterns[
                                              'ebooks_file'])

    move_files_to_directory(ebooks_files,
                            os.path.join(base_directory, 'Ebooks'),
                            verbose)


def executable_handling(verbose=True):
    """Handling of all executable files."""

    executable_files = list_files_by_patterns(base_directory,
                                              list_of_patterns[
                                                  'executable_files'])

    move_files_to_directory(executable_files,
                            os.path.join(base_directory, 'Executable'),
                            verbose)


def images_handling(verbose=True):
    """Handling of all images files."""

    image_files = list_files_by_patterns(base_directory,
                                         list_of_patterns['image_files'])

    move_files_to_directory(image_files,
                            os.path.join(base_directory, 'Images'),
                            verbose)


def pdfs_handling(verbose=True):
    """Handling of all PDFs files."""

    pdfs_files = list_files_by_patterns(base_directory,
                                        list_of_patterns[
                                            'pdf_file'])

    move_files_to_directory(pdfs_files,
                            os.path.join(base_directory, 'PDFs'),
                            verbose)


def scripts_handling(verbose=True):
    """Handling of all scripts files."""

    scripts_files = list_files_by_patterns(base_directory,
                                           list_of_patterns[
                                               'scripts_file'])

    move_files_to_directory(scripts_files,
                            os.path.join(base_directory, 'Scripts'),
                            verbose)


def videos_handling(verbose=True):
    """Handling of all videos files."""

    videos_files = list_files_by_patterns(base_directory,
                                          list_of_patterns[
                                              'video_files'])

    move_files_to_directory(videos_files,
                            os.path.join(base_directory, 'Videos'),
                            verbose)


if __name__ == "__main__":
    make_directories_for_organize()
    audios_handling()
    compressed_handling()
    ebooks_handling()
    executable_handling()
    images_handling()
    pdfs_handling()
    scripts_handling()
    videos_handling()
