import socket

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reuse address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
sock.bind( ('', 7777) )

# Listen
sock.listen(10)

while True:
	# Accept permintaan koneksi dari client
	conn, addr = sock.accept()
	# receive dari client
	data = conn.recv(20)
	print data
	# Tambahkan string OK
	data = "OK "+data
	# Kirim balik ke client
	conn.send(data)
	# Tutup koneksi
	# conn.close()
sock.close()

