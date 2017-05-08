import socket

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )

while True :
	data = raw_input("Masukkan textnya : ")
	# Kirim string
	sock.send(data)

	# Baca kembalian dari server
	data = sock.recv(100)
	print data
