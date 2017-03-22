import socket

# Inisiasi object socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Kirim data ke server
sock.sendto("Hello", ("127.0.0.1", 7777) )
# Terima dari server
data, address = sock.recvfrom(100)
# Cetak hasil
print data
# Close socket
sock.close()