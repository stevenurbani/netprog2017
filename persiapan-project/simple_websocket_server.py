from twisted.internet import protocol, reactor
from txws import WebSocketFactory

# List untuk menampung koneksi
clients = []

# Definisikan class untuk protocol yg akan kita buat
class EchoServer(protocol.Protocol) :
	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self) :
		print "Koneksi baru berhasil dibuat"
		# Jika terkoneksi, tambahkan client ke list koneksi
		clients.append(self)

	def connectionLost(self, reason) :
		print "Koneksi putus"
		# Jika koneksi putus, hapus client dari list koneksi
		clients.remove(self)

	# Callback func ketika ada message masuk dari client
	def dataReceived(self, data):
		print data
		data = "OK "+data
		# Untuk semua client di list koneksi, kirim data
		for cl in clients :
			cl.transport.write(data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, address) :
		return EchoServer()

factory = EchoFactory()
reactor.listenTCP(8877, WebSocketFactory(factory) )
reactor.run()