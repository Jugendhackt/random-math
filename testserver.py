#!/usr/bin/env python

# first version of server, this is getting improved soon, don't worry

import subprocess
from bottle import run, post, request, response, get, route

import trigonometrischeFunktionen


@route('/hello')
def hallo():
    return "Hello World!"


@route('/favicon.ico')
def icon():
    pass

"""
@route('/return2')
def other
"""

@route('/<path>', method = 'GET')
def process(path):
    if path == 'trigonometrie':
        pendel = trigonometrischeFunktionen.TrigonometriePendel()
        print pendel.anJson()
        return pendel.anJson()
    elif path == 'polynome':
        return "Hier kommen demnaechst polynome :P"

    # return subprocess.check_output(['python',path + '.py'])
    return "Nothing here yet! Come back later for more content!"


run(host='localhost', port=8080, debug=True)


