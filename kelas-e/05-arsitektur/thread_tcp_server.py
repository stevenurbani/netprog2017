import socket
from thread import start_new_thread

#Inisiasi objek socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding
sock.bind( ('',7778) )

# Listen
sock.listen(10)

def handle_connection(conn):
	try :
		while True :
			# Terima data dari client
			data = conn.recv(100)
			print data
			# Ubah data
			data = "OK "+data
			# Kirim balik ke client
			conn.send(data)
			# Tutup koneksi
	except socket.error :
		conn.close()
		print "Client telah memutuskan koneksi"

while True :
	# Accept permintaan 3-way handshaking
	conn, addr = sock.accept()
	# Buat thread baru
	start_new_thread(handle_connection, (conn,) )


	



