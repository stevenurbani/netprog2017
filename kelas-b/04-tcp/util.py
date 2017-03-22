import struct

def recvall_termination(conn):
	alldata = ''
	while True :
		data = conn.recv(10)
		if "\r\n" in data :
			alldata = alldata + data.replace("\r\n", "")
			return alldata
		alldata = alldata+data
	return alldata

def recvall_number(conn):
	msg_len_pack = conn.recv(4)
	msg_len = struct.unpack(">I", msg_len_pack)[0]
	print msg_len
	alldata = ""
	while len(alldata) < msg_len :
		alldata = alldata+conn.recv(10)
	return alldata

