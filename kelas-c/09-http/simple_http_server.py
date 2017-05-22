from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

# Definisikan class protocol
class EchoServer(LineReceiver) :
	first_line = True
	method = ''
	content_length = 0
	content = ""

	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self):
		print "Koneksi berhasil dibuat"

	# Callback func ketika data diterima
	def lineReceived(self, data) :
		print data

		if self.first_line :
			# bla bla bla
			parsed_data = data.split(' ')
			self.method = parsed_data[0]
			self.first_line = False
		else :
			# Baca content length dari header
			parsed_data = data.split(': ')
			if parsed_data[0] == "Content-Length" :
				self.content_length = int(parsed_data[1])

		if not data :
			self.first_line = True
			if self.method == 'GET':
				#bla bla bla
				#Kirim response ke client
				body = "Hello world"
				self.send_response(body)
			elif self.method == 'POST' :
				#Baca body dari request
				
				#Ubah modenya jadi mode raw
				self.setRawMode()

	def rawDataReceived(self, data):
		# Baca seluruh header
		self.content = self.content + data
		print data
		if len(self.content) >= self.content_length :
			# Kembali ke mode line
			self.setLineMode()
			# Kirim response ke client
			self.send_response("Anda mengirimkan data "+self.content)
			# Reset content
			self.content = ""

	def send_response(self, body) :
		length = len(body)
		self.transport.write("HTTP/1.1 200 OK\r\n")
		self.transport.write("Content-Length: "+str(length)+"\r\n")
		self.transport.write("\r\n")
		self.transport.write(body)


# Definisikan class factory
class EchoFactory(protocol.Factory):
	# Callback func ketika client baru terhubung
	def buildProtocol(self, address) :
		return EchoServer()

reactor.listenTCP(7777, EchoFactory())
reactor.run()