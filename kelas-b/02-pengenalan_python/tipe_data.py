a = 10
b = 20.0
c = 20

"""
d = a + b
#print "Hasil penjumlahannya adalah "+str(d)

d = a + c
#print d
"""


list_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
#print list_hari[0]
#for i in list_hari : 
#	print i

for i in range(0, len(list_hari)):
	if (i+1) % 2 != 0 :
		print list_hari[i]

"""
for i in range(0,3):
	print list_hari[i]
"""


"""
dict_ibukota = {"Indonesia" : "Jakarta", "Thailand" : "Bangkok", "Filipina" : "Manila"}
print dict_ibukota["Indonesia"]
for j in dict_ibukota :
	print j+" punya ibukota "+dict_ibukota[j]
"""