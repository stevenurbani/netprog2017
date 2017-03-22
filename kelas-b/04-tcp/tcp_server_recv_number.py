import socket
from util import recvall_termination, recvall_number
import struct

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reuse address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
sock.bind( ('', 7777) )

# Listen
sock.listen(10)

while True:
	# Accept permintaan koneksi dari client
	conn, addr = sock.accept()
	# receive dari client
	data = recvall_number(conn)
	print data
	# Tambahkan string OK
	data = "OK "+data

	# Cari panjang data yang akan dikirim
	msg_len = len(data)
	# Ubah dari integer ke data siap kirim pake pack
	msg_len_pack = struct.pack(">I", msg_len)
	# Tambahkan panjang data ke awal dari string
	data = msg_len_pack+data

	# Kirim balik ke client
	conn.send(data)
	# Tutup koneksi
	conn.close()
sock.close()

