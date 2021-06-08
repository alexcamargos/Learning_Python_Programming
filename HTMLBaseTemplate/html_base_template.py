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

root_files = ['index.html', 'README.md', 'LICENSE']
css_files = ['main.css']

root_dirs = ['assets']
sub_dirs = ['javascript', 'img', 'stylesheet']
javascript_files = None
img_files = None
stylesheet_files = ['main.css']

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

html_template = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>

</body>

</html>"""

readme_template = """# Project Name
Project description.

## View Project in Execution
You can check this website on this [link](https://#).

## Technologies
- HTML5
- CSS3
- JavaScript

## Prerequisites
You need a modern browser, just clone the repository, open the index.html
and edit it as you like. After edit share with me your version. :happy:

## License

Copyright (c) 2021 - **Alexsander Lopes Camargos**

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in 
all copies or substantial portions of the Software. 

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE. """

license_template = """The MIT License (MIT)

Copyright (c) 2021 - Alexsander Lopes Camargos

Permission is hereby granted, free of charge, to any person obtaining a 
copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions: 

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE. """


for file in root_files:
    if file == 'index.html':
        with open(file, 'w') as html_file:
            html_file.write(html_template)
    elif file == 'README.md':
        with open(file, 'w') as readme_file:
            readme_file.write(readme_template)
    else:
        with open(file, 'w') as license_file:
            license_file.write(license_template)


for base_dir in root_dirs:
    os.mkdir(base_dir)


os.chdir('assets')


for sub_dir in sub_dirs:
    os.mkdir(sub_dir)


os.chdir('stylesheet')


for file in stylesheet_files:
    with open(file, 'w') as stylesheet:
        stylesheet.write(copyright_banner)
