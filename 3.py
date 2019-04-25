# #10/4/2019
# #list
angka=[
    [1, 2, 3],
    [4, 5, 6],
    [7, [8, 9]]
]

print(angka[1][1]*angka[0][2]])
print(angka[2][1][0])

# a=[0, 2, 4, 'andi']
# b=[1, 3,5]
# print(a+b)
# print(a*2)

#tuple=immutable

# angkaList=[1,2,3,4,5,6]
# angkaTuple=[1,2,3,4,5,6]

# print(angkaList[0])
# print(angkaTuple[0])

# angkaList[0]=1234
# print(angkaList)

#angka[0]=1234           #tuple elementnya tidak dapat diubah
#print(angkaTuple)

#list bisa dicombine dengan tuple. list bisa didalam tuple atau sebaliknua
# angkaList=[
#     (1,2),
#     (3,4)
# ]

# angkaTuple=(
#     ['a','b'],
#     ['c','d']
# )

# print(angkaList[0][1])
# print(angkaTuple[1][1])

# angkaTuple[0][1]='andi'         #elemen di dalam tuple tidak bisa diubah. tetapi di dalam list bisa.
# print(angkaTuple)

#{a,b,c}    set

# data={1,2,3}
# print(data)
# print(type(data))

#untuk set itu no indexing. value variable nya tidak bisa diakses
#print(data[0])

#kesamaan antara list, set dan tuple adalah variabel ny bisa dicek
# dataL=[1,2,3]
# dataS={1,2,3}
# dataT=(1,2,3)

# print(2 in dataL)
# print(2 in dataS)
# print(2 in dataT)
# print(dataT[0:2:1])

# dataT+=dataT    #dataT=dataT+dataT
# print(dataT)

# dataT*=2        #dataT=dataT*2
# print(dataT)

dataS={'Andi','Budi','Caca'}

# for elemen in dataS:
#     print(elemen)

# dataS.add('Deni')           #karena set tidak punya index, jika di print akan ngacak2. add itu hanya bisa add 1 element
# dataS.update(['Euis', 'Fandi', 'Dika'])
# dataS.update({'Gani', 'Hesti'})
# print(dataS)

# dataS.remove('Euis')        #bedanya antara remove dan discard adalah kalau elemen yg di remove tidak ada, akan error. kalau discard g ada efek  
#dataS.discard('Budi')
# print(dataS)
# dataS.clear()

# del dataS
# print(dataS)

#[a,b,c] list=mutable
#(a,b,c) tuple=immutable
#{a,b,c} set=no indexing
#{'key':'value'} dictionary     bisa string/ integer atau kombinasi dr keduanya

namaHari={
    'monday':'senin',
    'tuesday':'selasa',
    'wednesday':'rabu'
}

# print(namaHari['monday'])
# print(namaHari.get('tuesday'))
# print(namaHari.get('friday','maaf data tidak tersedia'))

# namaHari['monday']='senin ceria'        #replace senin
# namaHari['thursday']='kamis'            #memasukkan variabel
# print(namaHari)

# namaHari.pop('monday')                  #menghapus variabel
# print(namaHari)


# print(namaHari.keys())
# print(list(namaHari.keys()))               #untuk mendapatkan list dari key nya
# print()
# print(namaHari.values())
# print(list(namaHari.values()))              #untuk mendapatkan list dari value nya
# print()
# print(namaHari['monday'])
# print(list(namaHari.keys())[list(namaHari.values()).index('senin')])

# #if statement
# sudahKerja=True

# if sudahKerja ==True:
#     print("traktiran dong")
# else:
#     print("sukses nyari kerja ya")

# job="PNS"

# if job=="PNS":
#     print("anda PNS")
# elif job=="swasta":
#     print("anda swasta")
# else:
#     print("anda nganggur")

# kerja=True
# jomblo=False

# if kerja and jomblo:
#     print('anda sudah kerja kok jomblo')
# elif kerja and not jomblo:
#     print('selamat')
# elif not kerja and jomblo:
#     print("mati aja kamu")
# else:
#     print('ya setidaknya punya pacar lah')

# #comparison
# a=12
# b=13
# c='12'

# print(a<=b)

# nilai=60
# #>=80 ==> lulus
# #>=60 tapi <=80 ==>remidial
# #<60==>ga lulus

# if nilai>=80:
#     print("nilai anda : ",nilai,".selamat anda lulus!")
# elif nilai <80 and nilai>=60:
#     print("nilai anda : ",nilai,". Anda harus remidial")
# else:
#     print("nilai anda : ",nilai,".Anda tidak lulus")

# angka=input('silahkan masukkan angka : ')

# if angka.isdigit():
#     if int(angka) %2==0:
#         print("angka",angka, "merupakan angka GENAP")
#     else :
#         print("angka",angka,"merupakan angka GANJIL")
# else:
#     print("maaf input tidak falid")


# # #membuat kalkulator
# var1=input("masukkan variabel 1 :")
# kon=input("masukkan konstanta (x,:,+,-) : ")
# var2=input("masukkan variabel ke 2 : ")

# if var1.isdigit() and var2 .isdigit():
#     print()
#     if kon.lower()=='x':
#         print(var1,"x",var2,"=",int(var1)*int(var2))
#     elif kon==':':
#         print(var1,":",var2,"=",int(var1)/int(var2))
#     elif kon=='+':
#         print(var1,"+",var2,"=",int(var1)+int(var2))
#     elif kon=='x':
#         print(var1,"-",var2,"=",int(var1)-int(var2))
#     else:
#         print('input yang anda masukkan salah.')
# else:
#     print('input yang anda masukkan salah.')

#membuat BMI
import math
berat=input("masukkan berat badan anda(kg) : ")
tinggi=input("masukkan tinggi anda (cm) : ")
print()
if berat.isdigit() and tinggi.isdigit():
    bmi=int(berat)/((int(tinggi)/100)**2)
    bmi=round(bmi,1)
    if bmi >=30:
        print("BMI anda =",bmi,". Anda kegemukan (obesitas).")
    elif bmi >=25 and bmi <30:
        print("BMI anda =",bmi,". Anda kelebihan berat badan.")
    elif bmi>=18.5 and bmi<25:
        print("BMI anda =",bmi,". Berat badan anda normal")
    else:
        print("BMI anda =",bmi,". Berat badan anda kurang.")
else:
    print("Input yang anda masukkan salah.")

