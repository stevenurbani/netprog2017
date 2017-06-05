from twisted.web import resource, server
from twisted.internet import reactor

# Protocol untuk handle HTTP
class Home(resource.Resource) :
	def render_GET(self, request) :
		return "OK"

	def render_POST(self, request) :
		print "Anda mengirimkan "+str(request.args)
		return "OK"

# Protocol untuk handle HTTP
class Sensor(resource.Resource) :
	def render_GET(self, request) :
		return "OK"

	def render_POST(self, request) :
		print "Anda mengirimkan "+str(request.args)
		return "OK"

# Factory
root = resource.Resource()
root.putChild('', Home())
root.putChild('sensor', Sensor())
site = server.Site(root)

# Reactor
reactor.listenTCP(8888, site)
reactor.run()