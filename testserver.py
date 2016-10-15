#!/usr/bin/env python

# first version of server, this is getting improved soon, don't worry

import subprocess
from bottle import run, post, request, response, get, route

import trigonometrischeFunktionen

def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*.*'
        # * in case you want to be accessed via any website
        return func(*args, **kwargs)
    return wrapper

@route('/hello')
def hallo():
    return "Hello World!"

@route('/favicon.ico')
def icon():
    pass

@route('/<path>', method = 'GET')
def process(path):
    if path == 'trigonometrie':
        pendel = trigonometrischeFunktionen.TrigonometriePendel()
        return pendel.anJson()
    elif path == 'gaussian'
        return "Hier kommen aufgaben zum gauss'schen Algorithmus"
    elif path == 'polynome':
        return "Hier kommen demnaechst polynome :P"

    # return subprocess.check_output(['python',path + '.py'])
    return "Nothing here yet! Come back later for more content!"


run(host='localhost', port=8080, debug=True)


