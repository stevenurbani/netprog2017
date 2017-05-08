import socket
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )
# Ambil inputan topik dari user
topik = raw_input("Masukkan topiknya : ")
# Kita buat dictionary message
dict_msg = {"topik" : topik, "tipe": "SUB"}
# Ubah jadi string
msg = json.dumps(dict_msg)
# Kirim message ke broker
sock.send(msg)
# Dapatkan status dari broker
status = sock.recv(100)
# Cek status
if status == "OK" :
	print "Subscribe berhasil"
else :
	print "Subscribe gagal"

while True :
	# Terima balasan dari server
	data = sock.recv(100)
	# Cetak data
	print data
