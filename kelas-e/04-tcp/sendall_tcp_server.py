import socket
from util import sendall_termination, recvall_termination
from util import sendall_number, recvall_number

#Inisiasi objek socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding
sock.bind( ('',7778) )

# Listen
sock.listen(10)

while True :
	# Accept permintaan 3-way handshaking
	conn, addr = sock.accept()
	# Terima data dari client
	data = recvall_number(conn)
	print data
	# Ubah data
	data = "OK "+data
	# Kirim balik ke client
	sendall_number(conn, data)
	# Tutup koneksi
	conn.close()



