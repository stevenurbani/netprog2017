import socket
import select

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reuse address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
sock.bind( ('', 7777) )

# Listen
sock.listen(10)

# Buat list untuk me-mantain semua koneksi atau I/O yang ada
list_koneksi = [sock]

while True :
	# inisiasi object select untuk memilih aktifitas I/O yang perlu ditangani
	inputready, outputready, errorready =  select.select(list_koneksi, [], [])

	for input_aktif in inputready :
		if input_aktif ==  sock :
			# Aktifitas socket utama
			conn, addr = sock.accept()
			# Tambahkan koneksi baru ke list koneksi yg harus dimonitor
			list_koneksi.append(conn)
		else :
			try :
				# Aktifitas yg berhubungan dengan koneksi ke client
				# Recv data dari client
				data = input_aktif.recv(100)
				print data
				# Ubah datanya
				data = "OK "+data
				# Kirim balik ke client
				input_aktif.send(data)
			except socket.error :
				# Remove koneksi dari list ketika client memutuskan koneksi
				list_koneksi.remove(input_aktif)
				print "Koneksi diputus oleh client"
