
arrpemasukkan = ["gaji", "bonus", "tunjangan", "pendapatan_lain"]
arrpengeluaran = ['konsumsi', 'transportasi', 'hiburan', 'pakaian', 'kesehatan', 'pendidikan']
def pemasukkan():
	totalpendapatan = 0
	data = []
	lanjut = "y"
	while lanjut == "y":
		print("Pilih Kategori pemasukkan")
		print("=========================")
		for i in range(0,len(arrpemasukkan)):
			print(i,arrpemasukkan[i])
		print("=========================")
		kategori_pemasukkan = input("masukkan angka :")
		katpemasukkan = kategori_pemasukkan
		# lanjut = "y"
		if katpemasukkan == "0":
			print ("Anda memilih pemasukkan",arrpemasukkan[0])
			pendapatan = int(input("Masukkan pendapatan gaji anda :"))
			totalpendapatan += pendapatan
			lanjut = input("ingin masukkan pendapatan lagi (y/n)?")

		elif katpemasukkan == "1":
			print ("Anda memilih pemasukkan",arrpemasukkan[1])
			pendapatan = int(input("Masukkan pendapatan bonus anda :"))
			totalpendapatan += pendapatan
			lanjut = input("ingin masukkan pendapatan lagi (y/n)?")

		elif katpemasukkan == "2":
			print ("Anda memilih pemasukkan",arrpemasukkan[2])
			pendapatan = int(input("Masukkan pendapatan tunjangan anda :"))
			totalpendapatan += pendapatan
			lanjut = input("ingin masukkan pendapatan lagi (y/n)?")

		elif katpemasukkan == "3":
			print ("Anda memilih pemasukkan",arrpemasukkan[3])
			pendapatan = int(input("Masukkan pendapatan lain anda :"))
			totalpendapatan += pendapatan
			lanjut = input("ingin masukkan pendapatan lagi (y/n)?")
		else:
			print("inputan tidak valid")
		data.append([kategori_pemasukkan,pendapatan])
		# lanjut = input("ingin masukkan pendapatan lagi (y/n)?")
def pengeluaran():
	totalpengeluaran = 0
	data2 = []
	lanjut = "y"
	while lanjut == "y":
		for i in range(0,len(arrpengeluaran)):
			print(i,arrpengeluaran[i])
		print("=========================")
		kategori_pengeluaran = input("masukkan angka :")
		katpengeluaran = kategori_pengeluaran

		if katpengeluaran == "0":
			print ("Anda memilih pengeluaran",arrpengeluaran[0])
			pengeluaran = int(input("Masukkan jumlah pengeluaran konsumsi anda :"))
			totalpengeluaran += pengeluaran
			lanjut = input("ingin masukkan pengeluaran lagi (y/n)?")

		elif katpengeluaran == "1":
			print("Anda memilih pengeluaran",arrpengeluaran[1])
			pengeluaran = int(input("Masukkan jumlah pengeluaran transportasi anda :"))
			totalpengeluaran += pengeluaran
			lanjut = input("ingin masukkan pengeluaran lagi (y/n)?")

		elif katpengeluaran == "2":
			print("Anda memilih pengeluaran",arrpengeluaran[2])
			pengeluaran = int(input("Masukkan jumlah pengeluaran hiburan anda :"))
			totalpengeluaran += pengeluaran
			lanjut = input("ingin masukkan pengeluaran lagi (y/n)?")

		elif katpengeluaran == "3":
			print("Anda memilih pengeluaran",arrpengeluaran[3])
			pengeluaran = int(input("Masukkan jumlah pengeluaran pakaian anda :"))
			totalpengeluaran += pengeluaran
			lanjut = input("ingin masukkan pengeluaran lagi (y/n)?")

		elif katpengeluaran == "4":
			print("Anda memilih pengeluaran",arrpengeluaran[4])
			pengeluaran = int(input("Masukkan jumlah pengeluaran kesehatan anda :"))
			totalpengeluaran += pengeluaran
			lanjut = input("ingin masukkan pengeluaran lagi (y/n)?")

		elif katpengeluaran == "5":
			print("Anda memilih pengeluaran",arrpengeluaran[5])
			pengeluaran = int(input("Masukkan jumlah pengeluaran pendidikan anda :"))
			totalpengeluaran += pengeluaran
			lanjut = input("ingin masukkan pengeluaran lagi (y/n)?")
		else:
			print("inputan tidak valid")
		data2.append([kategori_pengeluaran,pengeluaran])

def untungrugi():
		if(pemasukkan() > pengeluaran()):
			print("Anda untung bulan ini")
		else:
			print("Anda rugi bulan ini")

nama = input("masukkan nama anda: ")
print("1.Pemasukkan")
print("2.Pengeluaran")
print("3.Keuntungan dan Kerugian")
print("=================")
pilih = input("Pilih :")
if pilih == "1":
	print("=================")
	pemasukkan()
elif pilih == "2":
	print("=================")
	pengeluaran()
elif pilih == "3":
	print("=================")
	untungrugi()
	print("\n")
