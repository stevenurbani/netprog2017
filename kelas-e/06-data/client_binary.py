import socket
import struct

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kirim permintaan 3-way handshaking
sock.connect( ('127.0.0.1', 7778) )

angka = 1000000
data = struct.pack(">I", angka)

# Kirim string
sock.send(data)

# Baca kembalian dari server
data = sock.recv(100)
print data

# Tutup koneksi
sock.close()

	



