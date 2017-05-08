import socket
import select

#Inisiasi objek socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding
sock.bind( ('',7778) )

# Listen
sock.listen(10)
#Buat list untuk menampung semua koneksi yang dimonitor
list_koneksi = [sock]

while True :
	in_ready, out_ready, err_ready = select.select(list_koneksi, [], [])

	for s in in_ready :
		if s == sock :
			conn, address = s.accept()
			list_koneksi.append(conn)
		else :
			try :
				data = s.recv(100)
				data = "OK "+data
				s.send(data)
			except socket.error :
				list_koneksi.remove(s)
				print "Client memutuskan koneksi"
