import socket

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )

while True :
	data = raw_input("Input : ")
	# Kirim string ke server
	sock.send(data)
	# Terima balasan dari server
	data = sock.recv(100)
	# Cetak data
	print data
