from twisted.web.resource import Resource
from twisted.web import server
from twisted.internet import reactor

class Home(Resource):

	def render_GET(self, request):
		return "Selamat datang di halaman index"

class Mahasiswa(Resource):

	def render_GET(self, request) :
		return "Halaman Mahasiswa"

	def render_POST(self, request) :
		nama = request.args["nama"][0]
		return "Anda mengirimkan nama "+nama

# Daftarkan resource-nya

# Buat resource root
root = Resource()
root.putChild( "", Home() )
root.putChild( "mahasiswa",  Mahasiswa() )

# Buat komponen site
site = server.Site(root)

# Definisikan reactor
reactor.listenTCP(7777, site )
reactor.run()