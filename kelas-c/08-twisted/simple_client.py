import socket

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permintaan 3-way handshaking di sisi client
sock.connect( ('127.0.0.1', 7777) )
# Kirim string ke server
sock.send("Hello\r\n")
# Terima balasan dari server
data = sock.recv(100)
# Cetak balasan dari server
print data
# Tutup koneksi
sock.close()