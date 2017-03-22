# Deklarasi variabel berjenis integer
a = 10
# Deklarasi variabel berjenis double
b = 10.0
c = a + b
#print c
#print "Hasilnya adalah "+str(c)

# Deklarasi variabel berjenis string
x = "Hello world"
#print x

# Deklarasi variabel berjenis array/list
list_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
#print list_hari[2]
#for i in list_hari :
#	print i
for i in range(0, len(list_hari)):
	if (i+1) % 2 == 1:
		print list_hari[i]

# Deklarasi variabel berjenis dictionary
list_ibukota = {"Indonesia" : "Jakarta", "India" : "New Delhi", "Thailand" : "Bangkok"}
#print list_ibukota["Singapura"]
#for v in list_ibukota:
#	print v+" ibukotanya adalah "+list_ibukota[v]