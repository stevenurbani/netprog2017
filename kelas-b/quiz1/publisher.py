import socket
import json

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permintaan 3-way handshaking di sisi client
sock.connect( ('127.0.0.1', 7777) )
# Ambil inputan topik dan konten
topik = raw_input("Masukkan topiknya : ")
konten = raw_input("Masukkan kontennya : ")

# Bikin message bertipe dictionary
dict_msg = {"topik" : topik, "konten" : konten, "tipe":"PUB"}
# Ubah jadi string
msg = json.dumps(dict_msg)

# Kirim string ke broker
sock.send(msg)
# Terima balasan dari broker
data = sock.recv(1000)
# Cetak balasan dari broker
print data
# Tutup koneksi
sock.close()