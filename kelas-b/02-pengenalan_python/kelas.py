class Mobil(object):

	posisi = 0

	kecepatan = 10

	def maju(self):
		self.posisi = self.posisi + self.kecepatan

	def getPosisi(self):
		return self.posisi

mobilBaru = Mobil()
print mobilBaru.getPosisi()
mobilBaru.maju()
print mobilBaru.getPosisi()