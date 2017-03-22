class Mobil(object):

	def __init__(self, posisiAwal):
		self.posisi = posisiAwal

	posisi = 0

	kecepatan = 10

	def maju(self):
		self.posisi = self.posisi + self.kecepatan

	def getPosisi(self):
		return self.posisi

mobilBaru = Mobil(100)
print mobilBaru.getPosisi()
mobilBaru.maju()
print mobilBaru.getPosisi()