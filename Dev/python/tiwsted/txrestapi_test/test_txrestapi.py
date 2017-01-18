# -*- coding: utf-8 -*-
"""
    Created: 2016-12-23
    LastUpdate: 2016-12-23
    Filename: test_txrestapi
    Description: 
    
"""
from txrestapi.resource import APIResource
from twisted.web.server import Site
from twisted.internet import reactor
from twisted.web.server import Request

api = APIResource()
site = Site(api, timeout=None)


class FakeChannel(object):
    transport = None


def make_request(method, path):
    req = Request(FakeChannel(), None)
    req.prepath = req.postpath = None
    req.method = method
    req.path = path
    resource = site.getChildWithDefault(path, req)
    return resource.render(req)

reactor.listenTCP(8080, site)


def get_callback(request): return 'GET callback'
api.register('GET', '^/path/to/method', get_callback)


def post_callback(request): return 'POST callback'
api.register('POST', '^/path/to/method', post_callback)

reactor.run()
