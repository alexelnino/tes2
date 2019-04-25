'''
#8/4/2019
# variables

v=3j        #complex
w=True      #boolean
x=7500      #integer
y=12.34     #float
z='Andi'    #string

print(x)
print(y)
print(z)

#Variables
nama="Andi Susilowijaya Prakarsa"
usia=23
berat=76.8
jomblo=True
print("Hai saya "+nama+" .Umur saya "+str(usia)+"th")
print("Hai saya", nama, "umurku",usia,"th")
print()
#JUMAT
print('jum\'at')
print('Halo\tGaes')
print('Halo\nGaes')
print()
print(nama.lower())
print(nama.upper())
print(nama.islower())
print(nama.isupper())

print(len(nama))            #untuk menghitung jumlah karakter. spasi dihitung
print(nama[2])              #melihat huruf ketiga itu huruf apa. 0 itu huruf pertama
print(nama[len(nama)-1])
print(nama.index('A'))                  #mencari huruf A itu huruf keberapa
print(nama.replace('Andi','wijaya'))    #mengganti kata
print(nama.split(' '))                  #memotong spasi
print(nama.split(' ')[1])

#task
#penghitung jumlah huruf di nama seseorang (spasi tidak dihitung)
z=input("masukkan nama anda : ")
x=len(z)
y=z.split(' ')
z=len(y)-1
print('jumlah huruf di namamu : ',x-z)
#penghitung jumlah huruf tertentu di dalam suatu kata
nama=(input("masukkan nama anda : ")).lower()
huruf=(input("huruf yang dicari : ")).lower()
a=len(nama)
b=len(nama.split(huruf))-1
print('jumlah huruf di dalam suatu kata : ',b)

#9/4/2019
#cari jumlah karakter tertentu dalam suatu nama
nama='budi wicaksono'
cari='i'
namaTanpaCari=nama.lower().replace(cari.lower(),'')
jumlahCari=len(nama)-len(namaTanpaCari)

print('jumlah',cari,'dalam',nama,'adalah: ',jumlahCari)
'''
#cari jumlah kata tertentu dalam suatu kalimat
kalimat='kalimat : saya tidak masuk sekolah karena sekolah kebanjiran dan tidak ada guru'
print(kalimat)
print()
cari=input('kata yang dicari : ')
kataDicari=kalimat.lower().split(cari.lower())
jumlahKataDicari=len(kataDicari)-1
print('jumlah kata yang dicari yaitu',cari,'sebanyak',jumlahKataDicari,'kata')

