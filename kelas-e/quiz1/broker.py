import socket
from thread import start_new_thread
import json

#Inisiasi objek socket TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding
sock.bind( ('',7778) )

# Listen
sock.listen(10)

dict_sub = {}

def handle_connection(conn):	
	try :
		global dict_sub
		while True :
			# Terima data dari client
			data = conn.recv(100)
			#print data
			
			if data != "" :
				msg = json.loads(data)

				if msg["tipe"] == "SUB" :
					topik = msg["topik"]
					if topik in dict_sub :
						dict_sub[topik].append(conn)
					else :
						dict_sub[topik] = []
						dict_sub[topik].append(conn)
					conn.send("OK")
				elif msg["tipe"] == "PUB" :
					topik = msg["topik"]
					if topik in dict_sub :
						list_subscriber = dict_sub[topik]
						for sub in list_subscriber :
							sub.send(msg["konten"])
						conn.send("OK")
					else :
						conn.send("NOT OK")			
	except socket.error :
		for key in dict_sub :
			dict_sub[key].remove(conn)
		conn.close()
		print "Client telah memutuskan koneksi"

while True :
	# Accept permintaan 3-way handshaking
	conn, addr = sock.accept()
	# Buat thread baru
	start_new_thread(handle_connection, (conn,) )