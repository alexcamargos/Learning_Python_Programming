#  #!/usr/bin/env python
#  encoding: utf-8
#
#  ---------------------------------------------------------------------------
#  Name: rest_api_helloword_test.py
#  Version: 0.0.1
#  Summary: Testing a simple REST API making with Flask.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ---------------------------------------------------------------------------

"""Testing a Hello Word simple REST API making with Flask."""

import requests

BASE_URL = 'http://127.0.0.1:5000/'
ENDPOINT = 'helloword'
REQUEST_URL = BASE_URL + ENDPOINT

with requests.get(REQUEST_URL) as response_get:
    print(response_get.json())

with requests.post(REQUEST_URL) as response_post:
    print(response_post.json())

with requests.put(REQUEST_URL) as response_put:
    print(response_put.json())

with requests.delete(REQUEST_URL) as response_delete:
    print(response_delete.json())
