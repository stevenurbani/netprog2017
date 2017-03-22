import socket
import select

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding ke IP dan port tertentu
sock.bind( ('', 7778) )

# Listen
sock.listen(10)
# Buat list untuk menampung koneksi yang akan dimonitor oleh select
list_koneksi = [sock]

while True :
	inputready, outputready, errorready = select.select(list_koneksi, [], [])

	for n in inputready :
		# Jika input yg ready adalah socket server
		if n == sock :
			# Terima permintaan koneksi
			conn, addr = sock.accept()
			# Tambahkan koneksi baru ke list koneksi
			list_koneksi.append(conn)
		else :
			try :
				data = n.recv(100)
				print data
				data="OK "+data
				n.send(data)
			except socket.error:
				# Hapus koneksi yg putus dari list
				list_koneksi.remove(n)
				# Tutup koneksi ke client
				n.close()
				print "Koneksi ke client diputus"

