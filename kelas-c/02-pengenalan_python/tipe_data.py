a = 20
b = 10
c = 10.0

"""
d = a + b
print d

f = a + c
print f

x = "Hasil penjumlahannya adalah : "
print x+str(f)
"""

list_hari = ("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")
#print list_hari[0]
#for i in list_hari:
#	print i

#for j in range(0,len(list_hari)):
#	print list_hari[j]


dict_ibukota = {"Indonesia":"Jakarta", "Thailand":"Bangkok", "India" : "New Delhi"}
#print dict_ibukota["Thailand"]

#for i in dict_ibukota:
#	print i+' '+dict_ibukota[i]

try :
	print dict_ibukota["Malaysia"]
except KeyError:
	print "Index tidak ditemukan di dictionary"



