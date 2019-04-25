
# #9/4/2019
# #mempelajari angka
# x=12
# y=3

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)

# print(12**2)            #pangkat 2
# print(pow(12,2))        #pangkat 2
# print(abs(-1234))       #absolut

# z=8
# a=3
# print(z**(1/3))         #pangkat 3
# print(pow(z,1/a))       #pangkat 3
# a=0.1
# b=0.2
# print(a+b)              #error pada python
# print((a*10+b*10)/10)  #cara mensiasati error pada python. harusnya bener. g tau errornya dimana

# x=3.24689
# y=4.92872
# print(round(x))         #pembulatan
# print(round(y))
# print(round(x,2))       #pembulatan 2 digit di belakang koma
# print(round(y,2))

# #library:math (built-in)

# import math

# print(math.pi)              #3.14 atau 22/7
# print(math.sqrt(16))        #akar pangkat 2
# print(math.floor(2.98))     #pembulatan ke bawah=floor/lantai
# print(math.ceil(5.21))      #pembulatan ke atas=ceil/langit2

# z=6
# print(math.factorial(z))    #faktorial

# print(10%2)                 #sisa bagi/modulus
# print(10%3)
# print(10%4)

# #mempelajari input
# nama=input('halo, namamu siapa? : ')
# usia=input('halo '+nama+' ! usiamu berapa ? : ')
# x=float(usia)+20

# print('20 tahun lagi usia anda',x)

# #task menghitung equation yang simple
# total=int(input('Total usia = '))
# rasio=float(input('rasio usia = '))

# org1=int(total/(1+rasio))
# org2=int(total-org1)

# print('Usia org1 =',org1,'th dan usia org2 = ',org2,'th')


# #fungsi incremental
# x=12

# x+=1            #x=x+1
# print(x)

# x-=1            #x=x-1
# print(x)

# x*=2            #x=x*2
# print(x)

# x/=2            #x=x/2
# print(x)

#list
# x=12
# y=13
# z=14
# s=[x,y,z,21,23,25,99]           #s itu disebut list
# print(s)                        #yang didalam kurung kotak disebut variabel. variabel pertama dimulai dari 0
# print(len(s))                   #untuk menghitung jumlah variabel.
# print(s[0])                     #variabel urutan ke 0
# print(s[1])                     #variabel urutan ke 1
# print(s[2])                     #variabel urutan ke 2
# print()
# print(s[len(s)-1])              #untuk melihat variabel paling terakhir
# print(s[-1])                    #untuk melihat variabel paling terakhir

# print(s[0:3])           #start:end
# print(s[0:7:2])         #start:end:step
# print(s[::1])           #kita ingin menampilkan semua variabel tetapi kita tidak tahu dimulai dan diakhiri parameter keberapa
# print()

# students=['Andi','Budi','Caca','Budi']
# newStudents=['sifa','puji']
# additionalStudents='gilang'
# print(students.index('Budi'))
# print(students.index('Caca')            #caca urutan keberapa
# print(students.count('Budi'))           #menghitung budi ada berapa banyak di list  
# print(students)        
# students.extend(newStudents)            #memasukkan list ke dalam list
# print(students)

#students.append(additionalStudents)     #memasukkan kata string ke dalam list/variabel primitif. nambah nya ke paling belakang
#print(students)

# students.insert(3,'zaza')               #memasukkan variabel ke urutan ke 3
# print(students)

# students.remove('Budi')                 #menghilangkan variabel tetapi hanya 1
# print(students)

# students.clear()                       #delete all element
# students.pop()                          #delete last element
# students.pop(2)                         #delete element index ke-x

# students.sort()                         #urutkan element sesuai awal abjad
#students.reverse()                      #reverse by index

# print(students)

#mengurutkan angka di dalam list
# angka=[14,2,34,12,67,2]
# print(angka)

# x=angka[0:4]
# x.sort()
# print(x)

# angka[0:len(x)]=x
# print(angka)