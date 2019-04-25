'''
input("nama kamu? : ")
input("umur kamu? :")
import math
print(math.pi)              #phy=3.14
print(math.fabs(-4.7))      #bilangan positif
print(math.pow(8,2))        #8 pangkat 2
print(math.sqrt(64))        #akar kuadrat 64
print(round(4.7))           #pembulatan
print(round(4.4))           #pembulatan
print(math.floor(4.7))      #pembulatan ke bawah
print(math.ceil(4.4))       #pembulatan ke atas

#solve it 1
x=4
y=3
z=2
w=x+y*z/x*y
print(math.pow(w,z))

#solve it 2
x=input(" masukkan angka berapapun : ")
kuadrat_x=math.pow(int(x),2)
print("kuadrat dari",x,"=",kuadrat_x)

#solve it 3
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

#solve it 4
#a+b=49
#a/b=0.4
#print(a)

#solve it 6
import math
jarak=120
jam=9
a=60
b=40
jarak_bertemu=40/100*120
waktu_bertemu=jarak_bertemu/b
jam_bertemu=jam+waktu_bertemu
pembulatan_jam_bertemu=math.floor(jam_bertemu)
menit_bertemu=math.ceil((jam_bertemu-pembulatan_jam_bertemu)*60)
print("A dan B bertabrakan pada pukul",pembulatan_jam_bertemu,".",menit_bertemu)
'''
x = 5
y = '5'
z = 6
print(x==int(y) and int(y)<z);
print(x==int(y) or int(y)<z);
print(not(x==int(y) or int(y)<z));
