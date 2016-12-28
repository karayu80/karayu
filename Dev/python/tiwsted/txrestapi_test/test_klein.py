# -*- coding: utf-8 -*-
"""
    Created: 2016-12-27
    LastUpdate: 2016-12-27
    Filename: test_klein
    Description: 
    
"""
from klein import run, route


@route('/')
def home(request):
    return 'Hello, world'

@route('/user/<username>/test/<dataname>')
@route('/user/<username>')
def pg_user(request, username, dataname):
    return 'Hi %s!' % (username,)


@route('/user/bob')
def pg_user_bob(request):
    return 'Hello there 111!'



run('localhost', 8080)
