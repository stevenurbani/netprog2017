jumlah = input("Masukkan jumlah bintang : ")

for i in range(1, (jumlah+1)) :
	for j in range(1, (jumlah-i) ) :
		print "*",
	print ""