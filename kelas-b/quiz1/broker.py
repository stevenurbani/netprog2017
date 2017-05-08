import socket
from thread import start_new_thread
import json

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Reuse address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind
sock.bind( ('', 7777) )

# Listen
sock.listen(10)

dict_subs = {}

def handle_connection(conn):
	try :
		while True :
			# receive dari client
			data = conn.recv(1000)
			if data != "":
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
						conn.send("TIDAK ADA SUBSCRIBER")
	except socket.error :
		for key in dict_subs :
			dict_subs[key].remove(conn)
		conn.close()
		print "Client menutup koneksi"

try :
	while True:
		# Accept permintaan koneksi dari client
		conn, addr = sock.accept()
		start_new_thread(handle_connection, (conn,  ))
except KeyboardInterrupt :
	print "Server mati"
	
sock.close()

