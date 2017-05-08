import socket
from thread import start_new_thread
import json

# Inisiasi socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding ke IP dan port tertentu
sock.bind( ('', 7778) )

# Listen
sock.listen(10)

dict_subs = {}

def handle_connection(conn):
	try :
		while True :
			data = conn.recv(100)
			if data != "" :
				msg = json.loads(data)

				if msg["tipe"] == "SUB" :
					topik = msg["topik"]
					if topik in dict_subs :
						dict_subs[topik].append(conn)
					else :
						dict_subs[topik] = []
						dict_subs[topik].append(conn)
					conn.send("OK")
				elif msg["tipe"] == "PUB" :
					topik = msg["topik"]
					konten = msg["konten"]
					if topik in dict_subs :
						list_subs = dict_subs[topik]
						for sub in list_subs :
							sub.send(konten)
						conn.send("OK")
					else :
						conn.send("PUBLISH GAGAL")					
				else :
					conn.send("WRONG COMMAND")
	except socket.error :
		for key in dict_subs :
			dict_subs[key].remove(conn)
		conn.close()
		print "Koneksi ke client mati"


try :
	while True :
		# Accept permintaan 3-way handshaking
		conn, addr = sock.accept()
		# Buat thread baru untuk menghandle koneksi baru
		start_new_thread( handle_connection, (conn,) )
except KeyboardInterrupt :
	print "Server mati"
	
	