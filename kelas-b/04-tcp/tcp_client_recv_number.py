import socket
from util import recvall_termination, recvall_number
import struct

# TCP/IPv4
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Permintaan 3-way handshaking di sisi client
sock.connect( ('127.0.0.1', 7777) )
# Kirim string ke server
data = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cuius quidem, quoniam Stoicus fuit, sententia condemnata mihi videtur esse inanitas ista verborum. Quod autem principium officii quaerunt, melius quam Pyrrho; Duo enim genera quae erant, fecit tria. Tum Triarius: Posthac quidem, inquit, audacius. Si de re disceptari oportet, nulla mihi tecum, Cato, potest esse dissensio. Quae contraria sunt his, malane? Duo Reges: constructio interrete. An potest cupiditas finiri? Res enim fortasse verae, certe graves, non ita tractantur, ut debent, sed aliquanto minutius. Non igitur potestis voluptate omnia dirigentes aut tueri aut retinere virtutem."

# Cari panjang data yang akan dikirim
msg_len = len(data)
print "panjang dari client "+str(msg_len)
# Ubah dari integer ke data siap kirim pake pack
msg_len_pack = struct.pack(">I", msg_len)
# Tambahkan panjang data ke awal dari string
data = msg_len_pack+data

sock.send(data)
# Terima balasan dari server
data = recvall_number(sock)
# Cetak balasan dari server
print data
# Tutup koneksi
sock.close()