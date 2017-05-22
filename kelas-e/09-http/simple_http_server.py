from twisted.internet import reactor, protocol
from twisted.protocols.basic import LineReceiver

# Buat class untuk protocol yang kita definisikan
class EchoServer(LineReceiver) :
	content_length = 0
	first_line = True
	method = ''
	# Definisikan callback func.

	# Callback ketika koneksi berhasil dibuat
	def connectionMade(self):
		print "Satu koneksi baru ke client berhasil dibuat"

	def lineReceived(self, data) :
		print data
		if self.first_line :
			parsed_data = data.split(' ')
			self.first_line = False
			self.method = parsed_data[0]
		else :
			parsed_data = data.split(': ')
			if len(parsed_data) > 1 :
				if parsed_data[0] == 'Content-Length' :
					self.content_length = int(parsed_data[1])
		if not data :
			if self.method == 'GET':
				self.send_response('Hello')
			elif self.method == 'POST' :
				# Baca body nya
				pass

	
	def send_response(self,content):
		content_length = len(content)
		# kembalikan response nya
		self.sendLine("HTTP/1.1 200 OK")
		self.sendLine("Content-Length: "+str(content_length))
		self.sendLine('')
		self.transport.write(content)

		
# Buat class Factory baru
class EchoFactory(protocol.Factory) :
	def buildProtocol(self, address) :
		return EchoServer()

# Inisiasi reactor untuk looping
reactor.listenTCP(7777, EchoFactory())
reactor.run()