hari=int(input("masukkan jumlah hari : "))
import math
tahun=hari/360
round_tahun=math.floor(tahun)
# print(tahun)
# print(round_tahun)
bulan=(tahun-round_tahun)*360/30
round_bulan=math.floor(bulan)
# print(bulan)
# print(round_bulan)
minggu=(bulan-round_bulan)*30/7
round_minggu=math.floor(minggu)
# print(minggu)
# print(round_minggu)
hari_2=math.floor((minggu-round_minggu)*7)
# print(minggu)
# print(round_minggu)
# print(hari_2)
print(hari,"hari =",round_tahun,"tahun,",round_bulan,"bulan,",round_minggu,"minggu dan",hari_2,"hari.")