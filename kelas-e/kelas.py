class Mobil(object):

	kecepatan = 10

	posisi_x = 20

	def maju(self):
		self.posisi_x = self.posisi_x + self.kecepatan

	def getPosisi(self):
		return self.posisi_x

mobilSatu = Mobil()

print mobilSatu.getPosisi()
mobilSatu.maju()
print mobilSatu.getPosisi()

