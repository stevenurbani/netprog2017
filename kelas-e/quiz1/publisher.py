import socket
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )

# Ambil inputan topik dan konten
topik = raw_input("Masukkan topiknya : ")
konten = raw_input("Masukkan kontennya : ")

# Ubah ke bentuk json string
dict_msg = {"tipe" : "PUB", "topik": topik, "konten": konten}
msg = json.dumps(dict_msg)

# Kirim ke broker
sock.send(msg)

# Baca kembalian dari broker
data = sock.recv(100)
print data

# Tutup koneksi
#sock.close()