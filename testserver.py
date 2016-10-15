#!/usr/bin/env python

# first version of server, this is getting improved soon, don't worry

import subprocess
from bottle import run, post, request, response, get, route

import returnthis


@route('/hello')
def hallo():
    return "Hello World!"

"""
@route('/return2')
def other
"""

@route('/<path>', method = 'GET')
def process(path):
    if path == 'return':
        return returnthis.func()
    elif path == 'trigonometrie':
        return returnthis.func()
    elif path == 'polynome':
        pass

    return subprocess.check_output(['python',path + '.py'])


run(host='localhost', port=8080, debug=True)


