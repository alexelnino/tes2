# # #function

# # def tes(x):
# #     print('halo',x)

# # tes('andi')
# # tes(input('ketik nama : '))
# # print(tes('andi'))

# # def tes(x,y):
# #     z=x**y
# #     print('hasil kali',x, 'dan',y , 'adalah',x*y)
# #     print('hasil',x,'pangkat',y,'=',z)

# # tes(2,3)                      #kalau pakai command print tidak akan muncul di terminal / none.contoh print(tes(2,3))

# # import math
# # def luasLingkaran(r):
# #     luas=math.pi*r**2
# #     print('luas lingkaran dengan jari-jari',r,'adalah',luas)

# # luasLingkaran(7)

# # def luasTrapesium(a,b,t):
# #     luas=(a+b)*t/2
# #     print('luas trapesium dengan a =',a,'t =',t,'dan b =',b,'adalah',luas)

# # luasTrapesium(2,3,5)

# # #return function
# # def aloha():
# #     print('halo andi')

# # print(type(aloha()))
# # def hai():
# #     return 'halo andi'          #kalau menggunakan return maka akan bisa di print

# # hai()
# # print(hai())

# # def hola(nama):
# #     return 'halo '+ nama
# # print(hola('caca'))


# # def kuadrat(x):
# #     return x**2

# # print(kuadrat(4)+kuadrat(3))
# # print(kuadrat(5))

# kurs={
#     '1':0.000071,
#     '2':14157
# }
# def konversi():
#     print('selamat datang di webkonversi.com')
#     print('silahkan pilih metode konversi')
#     print('1. IDR ke USD')
#     print('2. USD ke IDR')
#     metode=input('ketik pilihan anda : ')
#     if metode=='1':
#         nominal=input('ketik nominal rupiah : Rp ')
#         if nominal.replace('.','').replace(',','').isdigit():
#             hasil=float(nominal.replace(',','.'))*kurs[metode]
#             print('konversi Rp',nominal,'=$',hasil)
#         else:
#             print('mohon hanya input angka')
#     elif metode=='2':
#         nominal=input('ketik nominal dolar : $ ')
#         if nominal.replace('.','').replace(',','').isdigit():
#             hasil=float(nominal.replace(',','.'))*kurs[metode]
#             print('konversi $',nominal,'=Rp',hasil)       
#         else:
#             print('mohon hanya input angka')
#     else:
#         print('metode yang anda pilih tidak tersedia')

# konversi()


# #string formatting method di python
# x=2000000
# print(x)
# print('{:,}'.format(x))
# print('{:,}'.format(x).replace(',','.'))

# print('halo {}, umurmu {}'.format('Andi',27))
# print('halo {1}, umurmu {0}'.format('Andi',27))
# print('asalmu dari {kota}'.format(kota='Jakarta'))
# print('suhu udara = {:f}'.format(25))

# x='halo {:s}'
# print(x.format('andi'))

# #looping #1
# angka=1
# while angka<=10:
#     print('haha ke-',angka)
#     angka+=1

# angka=[11,22,23,24,25,26,27]
# angka2=[]
# i=0
# while i<=len(angka)-1:
#     print(angka[i]*2)
#     i+=1

# angka=[11,22,23,24,25,26,27]
# i=0
# while i<=len(angka)-1:
#     angka2.append(angka[i]*2)
#     i+=1

# print(angka)
# print(angka2)

i=0
while i<=6:
    print(i)
    if i==4:
        break
    i+=1
print()
i=0
while i<=6:
    i+=1
    if i==4:
        continue
    print(i)

#looping #2
#for loop

# kata='andilala'
# for huruf in kata:
#     print(huruf)
# print()
# angka=[12,24,36,45,54,63]
# for z in angka:
#     print(z)
# print()
# for data in range(5,10):
#     print('haha ke-',data)
# print()
# for data in range(5,10,2):
#     print('haha ke-',data)

# angka=[11,22,33,44,55,66]
# for x in angka:
#     print(x)
# print()
# for i in range(len(angka)):
#     print(angka[i])

# star=''
# for i in range(5):
#     star+=' * '
#     print(star)

# angka=''
# for i in range(5):
#     angka=angka+str(i)+' '

# for i in range(5):
#     for j in range(5):
#         print(i ,'dan' ,j)

#tugas bikin segitiga terbalik menggunakan bintang
#

# angka=''
# for i in range(5):
#     angka=angka+str(i)+ ' '
#     print(angka)

string = ""
bar = 1

x = int(input("Masukkan angka :"))
no = 1
# Looping Baris
while bar <= x:
	kol = bar
	# Looping Kolom
	while kol > 0:
		string = string + " " + str(no) + " "
		kol = kol - 1

	string = string + "\n"
	bar = bar + 1
	no = no+1
print (string)

