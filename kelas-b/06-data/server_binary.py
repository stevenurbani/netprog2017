import socket
from thread import start_new_thread
import struct

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reuse address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
sock.bind( ('', 7777) )

# Listen
sock.listen(10)

def handle_connection(conn):
	try :
		while True :
			# receive dari client
			data = conn.recv(4)
			if data != "" :
				angka = struct.unpack(">I", data)[0]

				hasil = 5*angka

				print hasil
				# Tambahkan string OK
				data = "OK "+str(hasil)
				# Kirim balik ke client
				conn.send(data)
				# Tutup koneksi
				# conn.close()
	except socket.error :
		conn.close()
		print "Client menutup koneksi"

try :
	while True:
		# Accept permintaan koneksi dari client
		conn, addr = sock.accept()
		start_new_thread(handle_connection, (conn,  ))
except KeyboardInterrupt :
	print "Server mati"
	
sock.close()

