import json

'''
Untuk mengirimkan sebuah data berstruktur, kita dapat menggunakan bentuk JSON.
JSON merupakan data berstruktur dalam bentuk text/string.
String JSON dapat dibuat dari tipe data dictionary
'''

dict_contoh = {
	"nama" : "Adhitya",
	"jurusan" : "Informatika"
}

# Ubah menjadi string JSON sebelum dikirim lewat socket.send()

text_json = json.dumps(dict_contoh)

print text_json

# Oleh receiver, data diterima dalam bentuk string JSON
# Untuk mengubah kembali menjadi dictionary, kita bisa 
# memanfaatkan fungsi json.loads()

dict_hasil = json.loads(text_json)

print dict_hasil['nama']+" "+dict_hasil["jurusan"]
