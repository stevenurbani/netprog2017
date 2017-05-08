from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

# Definisikan class untuk protocol yg akan kita buat
class EchoServer(LineReceiver) :
	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self) :
		print "Koneksi baru berhasil dibuat"

	# Callback func ketika ada message masuk dari client
	def lineReceived(self, data):
		print data
		#data = "OK "+data
		self.transport.write("Hello") 

class EchoFactory(protocol.Factory):
	def buildProtocol(self, address) :
		return EchoServer()

reactor.listenTCP(7777, EchoFactory())
reactor.run()