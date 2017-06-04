from twisted.internet import protocol, reactor
from txws import WebSocketFactory

# Definisikan class protocol
class EchoServer(protocol.Protocol) :
	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self):
		print "Koneksi berhasil dibuat"

	# Callback func ketika data diterima
	def dataReceived(self, data) :
		print data
		data = "OK "+data
		# Kirim balik ke client
		self.transport.write(data)

# Definisikan class factory
class EchoFactory(protocol.Factory):
	# Callback func ketika client baru terhubung
	def buildProtocol(self, address) :
		return EchoServer()

factory = EchoFactory()
reactor.listenTCP(7788, WebSocketFactory(factory))
reactor.run()