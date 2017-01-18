# -*- coding: utf-8 -*-
"""
    Created: 2017-01-17
    LastUpdate: 2017-01-17
    Filename: test_non_blocking
    Description: 
    
"""
from twisted.internet import reactor, threads
from twisted.internet.task import deferLater, defer
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET

import time
import pycurl
import certifi
from StringIO import StringIO

_count = 0


class BusyPage(Resource):
    isLeaf = True

    def _error_callback(self, failure, request):
        print failure
        request.write("_error_callback Finally done, at %s" %(time.asctime(), ))
        request.finish()

    def _delaydRender(self, request):
        request.write("_delaydRender Finally done, at %s" %(time.asctime(), ))
        request.finish()

    def _ping(self):
        return "ok count: {}".format(_count)

    def _pycurl(self, request):
        access_token = 'abcd'
        str_my_ip = '10.10.10.1'
        _buffer = StringIO()

        c = pycurl.Curl()
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.URL, 'https://i-auth.iam4.com/v1.0/common/session')
        c.setopt(c.HTTPHEADER, ['Sg-Param-Access-Token: {}'.format(access_token),
                                'Sg-Param-Ip: {}'.format(str_my_ip)])

        c.setopt(c.WRITEDATA, _buffer)
        c.perform()
        c.close()

        # request.write("_pycurl Finally done, at %s" %(time.asctime(), ))
        # request.finish()

    def render_GET(self, request):
        global _count

        print request.uri
        if request.uri == '/ping':
            _count+=1
            return self._ping()

        # d = deferLater(reactor, 5, lambda: request)
        # d.addCallback(self._delaydRender)

        # threads.deferToThread(self._delaydRender, request)

        # d = defer.Deferred()
        # d.addCallback(self._delaydRender)
        # d.callback(request)

        # d = deferLater(reactor, 1, self._pycurl, request)
        # d.addCallback(self._delaydRender, request)
        # d.addErrback(self._error_callback, request)

        # d = deferLater(reactor, 1, self._pycurl, request)
        # d.addCallback(self._delaydRender, request)
        # d.addErrback(self._error_callback, request)

        d = threads.deferToThread(self._pycurl, request)
        d.addCallback(self._delaydRender, request)
        d.addErrback(self._error_callback, request)
        return NOT_DONE_YET


class DelayedResource(Resource):
    isLeaf = True

    def _delayedRender(self, request):
        request.write("<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()
        request.finish()


    def _responseFailed(self, err, call):
        print err
        call.cancel()

    def render_GET(self, request):
        call = reactor.callLater(5, self._delayedRender, request)
        request.notifyFinish().addErrback(self._responseFailed, call)
        return NOT_DONE_YET

factory = Site(DelayedResource())
reactor.listenTCP(8000, factory)
reactor.run()
