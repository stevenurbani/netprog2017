from twisted.web import resource, server
from twisted.internet import reactor

# Protocol untuk handle HTTP
class Home(resource.Resource) :
	def render_GET(self, request) :
		return "Halaman index"

	def render_POST(self, request) :
		return "Anda mengirimkan "+str(request.args)

# Protocol untuk handle HTTP
class Mahasiswa(resource.Resource) :
	def render_GET(self, request) :
		return "Halaman mahasiswa"

	def render_POST(self, request) :
		return "Anda mengirimkan "+str(request.args)

# Factory
root = resource.Resource()
root.putChild('', Home())
root.putChild('mahasiswa', Mahasiswa())
site = server.Site(root)

# Reactor
reactor.listenTCP(8888, site)
reactor.run()