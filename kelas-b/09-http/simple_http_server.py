from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

# Definisikan class untuk protocol yg akan kita buat
class EchoServer(LineReceiver) :
	first_line = True
	method = ''
	content_length = 0
	content = ''

	# Callback func ketika koneksi berhasil dibuat
	def connectionMade(self) :
		print "Koneksi baru berhasil dibuat"

	# Callback func ketika ada message masuk dari client
	def lineReceived(self, data):
		print data
		if self.first_line :
			#bla bla bla
			parsed_data = data.split(' ')
			self.method = parsed_data[0]
			self.first_line = False
		else :
			# bla bla bla
			parsed_data = data.split(': ')
			if parsed_data[0] == "Content-Length" :
				self.content_length = int(parsed_data[1])

		# Jika header sudah dibaca semua
		if not data :
			self.first_line = True
			# Cek method HTTP-nya
			if self.method == 'GET' :
				# bla bla bla
				body = "Hello world"
				self.send_response(body)
			elif self.method == 'POST' :
				# bla bla bla
				# Reset value dari variabel content
				self.content = ''
				# Ubah jadi mode raw
				self.setRawMode()

	def rawDataReceived(self, data):
		self.content = self.content+data

		if len(self.content) >= self.content_length :
			# Pindah ke mode line lagi
			self.setLineMode()
			# Print data yang diterima
			print self.content
			# Kembalikan response ke client
			self.send_response("Data yg dikirim : "+self.content)


	def send_response(self, body):
		content_length = len(body)
		# Kembalikan responsenya ke client
		self.transport.write("HTTP/1.1 200 OK\r\n")
		self.transport.write("Content-Length: "+str(content_length)+"\r\n")
		self.transport.write("\r\n")
		# Kirim body response
		self.transport.write(body)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, address) :
		return EchoServer()

reactor.listenTCP(7777, EchoFactory())
reactor.run()