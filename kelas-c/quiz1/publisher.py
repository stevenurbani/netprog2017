import socket
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )
# Ambil inputan dari user
topik = raw_input("Masukkan topik : ")
konten = raw_input("Masukkan konten : ")
# Definisikan message dalam bentuk dictionary
dict_msg = {"tipe" : "PUB", "topik" : topik, "konten": konten}
# Ubah jadi string
msg = json.dumps(dict_msg)
# Kirim string ke broker
sock.send(msg)
# Terima balasan dari server
data = sock.recv(100)
# Cetak data
print data
# Tutup koneksi
sock.close()