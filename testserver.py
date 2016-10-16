#!/usr/bin/env python

# first version of server, this is getting improved soon, don't worry

import subprocess
from bottle import Bottle, run, post, request, response, get, route

import trigonometrischeFunktionen, curve_sketching, linerareGleichungsSysteme, vektoren

def allow_cors(func):
    """ this is a decorator which enable CORS for specified endpoint """
    def wrapper(*args, **kwargs):
        response.headers['Access-Control-Allow-Origin'] = '*'
        # * in case you want to be accessed via any website
        return func(*args, **kwargs)
    return wrapper

@route('/hello')
@allow_cors
def hallo():
    return "Hello World!"

@route('/favicon.ico')
@allow_cors
def icon():
    pass

@route('/<path>', method = 'GET')
@allow_cors
def process(path):
    if path == 'trigonometrie':
        pendel = trigonometrischeFunktionen.TrigonometriePendel()
        return pendel.anJson()
    if path == 'gaussian':
        return "Hier kommen aufgaben zum gauss'schen Algorithmus"
    if path == 'polynome1':
        return curve_sketching.generatePolynomeExercise(1)
    if path == 'polynome2':
        return curve_sketching.generatePolynomeExercise(2)
    if path == 'polynome3':
        return curve_sketching.generatePolynomeExercise(3)
    if path == 'linearegls':
        gls = linerareGleichungsSysteme.LGS()
        return gls.anJson()
    if path == 'vector':
        vec = vektoren.Vektoren()
        return vec.anJson()
    if path == 'numbers':
        pass

    # return subprocess.check_output(['python',path + '.py'])
    return "Nothing here yet! Come back later for more content!"


run(host='localhost', port=61535, debug=True)


