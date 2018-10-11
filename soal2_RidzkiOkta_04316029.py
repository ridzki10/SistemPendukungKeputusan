arrjalan = [{"dari":"0", "ke":"1", "jarak": 13},
		{"dari":"0", "ke":"2", "jarak": 4}, 
		{"dari":"1", "ke":"3", "jarak": 6}, 
		{"dari":"1", "ke":"2", "jarak": 2},
		{"dari":"2", "ke":"4", "jarak": 1},
		{"dari":"3", "ke":"5", "jarak": 5},
		{"dari":"4", "ke":"3", "jarak": 5},
		{"dari":"4", "ke":"5", "jarak": 13}]

def filterArrayList(item, value):
	return [i for i in arrjalan if i[item] == value]

dari = "0"
ke = "5"
jarakTempuh = ""
jarakTotal = 0

# terkecil
while dari != ke:
	data = filterArrayList("dari", dari)
	hasil = ""
	hasilList = []
	for i in data:
		a = i["jarak"]
		if(a != hasil):
			hasil = a
			hasilList = i
	jarakTempuh = jarakTempuh + "Dari "+dari+" ke "+hasilList["ke"]+", "
	jarakTotal = jarakTotal + int(hasilList["jarak"])
	dari = hasilList["ke"]
print (jarakTempuh)
print (jarakTotal)
