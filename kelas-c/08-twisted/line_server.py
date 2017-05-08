from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

# Definisikan class protocol
class EchoServer(LineReceiver) :
	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self):
		print "Koneksi berhasil dibuat"

	# Callback func ketika data diterima
	def lineReceived(self, data) :
		print data
		data = "OK "+data
		# Kirim balik ke client
		self.transport.write(data)

# Definisikan class factory
class EchoFactory(protocol.Factory):
	# Callback func ketika client baru terhubung
	def buildProtocol(self, address) :
		return EchoServer()

reactor.listenTCP(7777, EchoFactory())
reactor.run()