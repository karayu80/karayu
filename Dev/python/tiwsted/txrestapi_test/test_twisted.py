from twisted.web import server, resource
from twisted.internet import reactor, endpoints
from twisted.web.resource import Resource


class Simple(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        return "<html>Hello, world!</html>"

class Hello(Resource):
    isLeaf = True
    def getChild(self, name, request):
        if name == '':
            print 'hit {}'.format(name)
            return self
        return Resource.getChild(self, name, request)

    def render_GET(self, request):
        return "Hello, I am located at {}".format(request.uri)

    # def render_GET(self, name, request):
    #     return "name Hello, I am located at {}".format(request.uri)

root = Hello()
root.putChild('fred', Hello())
root.putChild('bob', Hello())

site = server.Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(site)
reactor.run()