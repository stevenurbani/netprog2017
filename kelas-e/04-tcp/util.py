import struct

def sendall_termination(conn, data):
	termination_char = "\r\n"
	data = data+termination_char
	conn.send(data)

def recvall_termination(conn):
	alldata = ""
	temp_data = ""

	while "\r\n" not in temp_data :
		temp_data = conn.recv(10)
		alldata = alldata+temp_data

	return alldata

def sendall_number(conn, data):
	msg_size = len(data)
	msg_size_packed = struct.pack(">I", msg_size)
	data = msg_size_packed+data
	conn.send(data)

def recvall_number(conn):
	msg_size_packed = conn.recv(4)
	msg_size = struct.unpack(">I", msg_size_packed)[0]

	alldata = ""

	while len(alldata) < msg_size :
		alldata = alldata + conn.recv(10)

	return alldata