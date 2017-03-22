import socket
from thread import start_new_thread

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding ke IP dan port tertentu
sock.bind( ('', 7778) )

# Listen
sock.listen(10)

def handle_connection(conn):
	try :
		while True :
			# Receive data dari client
			data = conn.recv(100)
			print data
			# Ubah datanya
			data = "OK "+data
			# Kirim balik ke client
			conn.send(data)
	except socket.error :
		conn.close()
		print "Koneksi ke client mati"


try :
	while True :
		# Accept permintaan 3-way handshaking
		conn, addr = sock.accept()
		# Buat thread baru untuk menghandle koneksi baru
		start_new_thread( handle_connection, (conn,) )
except KeyboardInterrupt :
	print "Server mati"
	
	