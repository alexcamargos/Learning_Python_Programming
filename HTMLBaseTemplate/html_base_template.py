#  #!/usr/bin/env python
#  encoding: utf-8
#
#  ---------------------------------------------------------------------------
#  Name: html_base_template.py
#  Version: 0.0.1
#  Summary:
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ---------------------------------------------------------------------------

import os

root_files = ['index.html',
              'README.md',
              'LICENSE',
              '.gitignore',
              '.editorconfig']

template_files = ['html',
                  'readme',
                  'license']

stylesheet_files = ['main.css']

javascript_files = None
img_files = None

root_dirs = ['assets']
sub_dirs = ['javascript',
            'stylesheet',
            'img']

copyright_banner = """/*
# -------------------------------------------------------------------------------------------------
#
# Name: main.css
# Version: 0.0.1
#
# Summary:
#
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# -------------------------------------------------------------------------------------------------
*/"""


def create_file(file_name, content):
    """Create the file in the directory using the given content."""

    with open(file_name, 'w') as _fn:
        _fn.write(content)


with open(r'D:\WORKSPACE\Python\LearningPythonProgramming\HTMLBaseTemplate\template\html') as _fn:
    html_template = _fn.read()

with open(r'D:\WORKSPACE\Python\LearningPythonProgramming\HTMLBaseTemplate\template\readme') as _fn:
    readme_template = _fn.read()

with open(r'D:\WORKSPACE\Python\LearningPythonProgramming\HTMLBaseTemplate\template\license') as _fn:
    license_template = _fn.read()

with open(r'D:\WORKSPACE\Python\LearningPythonProgramming\HTMLBaseTemplate\template\gitignore') as _fn:
    gitignore_template = _fn.read()

with open(r'D:\WORKSPACE\Python\LearningPythonProgramming\HTMLBaseTemplate\template\editorconfig') as _fn:
    editorconfig_template = _fn.read()

for file in root_files:
    if file == 'index.html':
        create_file(file, html_template)
    elif file == 'README.md':
        create_file(file, readme_template)
    elif file == '.gitignore':
        create_file(file, gitignore_template)
    elif file == '.editorconfig':
        create_file(file, editorconfig_template)
    else:
        create_file(file, license_template)

for base_dir in root_dirs:
    os.mkdir(base_dir)

os.chdir('assets')

for sub_dir in sub_dirs:
    os.mkdir(sub_dir)

os.chdir('stylesheet')

for file in stylesheet_files:
    with open(file, 'w') as stylesheet:
        stylesheet.write(copyright_banner)
