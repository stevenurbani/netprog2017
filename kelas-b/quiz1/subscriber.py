import socket
import json

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permintaan 3-way handshaking di sisi client
sock.connect( ('127.0.0.1', 7777) )
# Ambil topik dari inputan user
topik = raw_input("Masukkan topiknya : ")
# Buat dictionary message untuk subscrption
dict_msg = {"topik" : topik, "tipe" : "SUB"}
# Ubah dict jadi string
msg = json.dumps(dict_msg)
# Kirim pesan subscription ke broker
sock.send(msg)
# Terima kembalian dari broker
data = sock.recv(1000)
# Cek kembaliannya
if data == "OK" :
	print "Subscribe berhasil"
else :
	print "Subscribe gagal"

while True :
	# Terima message dari broker
	data = sock.recv(1000)
	# Cetak balasan dari server
	print data
	