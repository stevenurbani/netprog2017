import socket

#Inisiasi objek socket UDP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind server ke IP dan port tertentu
sock.bind( ('', 7777) )

try :
	# Buat service-nya jalan terus
	while True :
		# Baca data yang sudah dikirimkan oleh client
		# return value : data dan alamat pengirim
		data, address = sock.recvfrom(100)
		print "Server menerima data "+data+" dari client"
		# Ubah data
		data = "OK "+data
		#Kirim balik ke client
		sock.sendto(data, address)
except KeyboardInterrupt :
	sock.close()
	print "Server mati"

