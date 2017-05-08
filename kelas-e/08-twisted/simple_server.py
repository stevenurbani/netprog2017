from twisted.internet import reactor, protocol

# Buat class untuk protocol yang kita definisikan
class EchoServer(protocol.Protocol) :
	# Definisikan callback func.

	# Callback ketika koneksi berhasil dibuat
	def connectionMade(self):
		print "Satu koneksi baru ke client berhasil dibuat"

	# Callback ketika message dari client masuk
	def dataReceived(self, data) :
		print data
		data = "OK "+data
		# Kirim balik ke client pakai Transport
		self.transport.write(data)

# Buat class Factory baru
class EchoFactory(protocol.Factory) :
	def buildProtocol(self, address) :
		return EchoServer()

# Inisiasi reactor untuk looping
reactor.listenTCP(7777, EchoFactory())
reactor.run()