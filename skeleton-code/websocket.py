from twisted.internet import protocol, reactor
from txws import WebSocketFactory

# Definisikan class untuk protocol yg akan kita buat
class EchoServer(protocol.Protocol) :
	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self) :
		print "Koneksi baru berhasil dibuat"

	def connectionLost(self, reason) :
		print "Koneksi putus"

	# Callback func ketika ada message masuk dari client
	def dataReceived(self, data):
		print data
		

class EchoFactory(protocol.Factory):
	def buildProtocol(self, address) :
		return EchoServer()

factory = EchoFactory()
reactor.listenTCP(8877, WebSocketFactory(factory) )
reactor.run()