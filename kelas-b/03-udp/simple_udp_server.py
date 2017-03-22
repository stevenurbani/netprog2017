import socket

# Inisiasi object socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# Mengikat ke alamatIP/port tertentu
sock.bind( ('', 7777) )

try :
	print "Server hidup"
	while True:
		#Baca data yang dikirimkan oleh client
		data, address = sock.recvfrom(100)
		#Olah data yang diterima
		print "Menerima "+data+" dari client"
		data = "OK "+data
		# Kirim balik ke client
		sock.sendto(data, address)
except KeyboardInterrupt :
	print "Server mati"

