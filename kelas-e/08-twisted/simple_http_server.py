from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

# Buat class untuk protocol yang kita definisikan
class EchoServer(LineReceiver) :
	# Definisikan callback func.

	# Callback ketika koneksi berhasil dibuat
	def connectionMade(self):
		print "Satu koneksi baru ke client berhasil dibuat"

	def lineReceived(self, data) :
		print data
		#self.transport.write("OK "+data)

# Buat class Factory baru
class EchoFactory(protocol.Factory) :
	def buildProtocol(self, address) :
		return EchoServer()

# Inisiasi reactor untuk looping
reactor.listenTCP(7777, EchoFactory())
reactor.run()