import socket
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )

topik = raw_input("Masukkan topiknya : ")

# Definisikan message untuk subscription
dict_msg = {"tipe" : "SUB", "topik" : topik}
msg = json.dumps(dict_msg)

# Kirim pesan untuk subscription ke broker
sock.send(msg)
data = sock.recv(100)

# Cek return valuenya
# Jika OK, berarti subscription berhasil
if data == "OK" :
	print "Subscribe berhasil"
else :
	print "Subscribe gagal" 

while True :
	# Baca kembalian dari server
	data = sock.recv(100)
	print data