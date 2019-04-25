# # #2.py
# # #mempelajari angka
# # x=2.2324
# # y=3
# # print(x**3)
# # print(abs(-232))

# # print(round(x,2))
# # import math
# # print(math.pi)
# # print(math.ceil(x))
# # print(math.ceil(x))

# # print(10%3)

# # a=0.1
# # b=0.2
# # print(a+b)              #error pada python
# # print((a*10+b*10)/10)

# # #list
# # x=[2,4,73,234,43,32,32]
# # x.append(2)
# # print(x)
# # print(x.count(2))
# # y=2,3,4,5


# # print(len(x))

# # print(x[1])
# # print(x[-3])
# # print(x[::1])

# # #list string
# # a=['alfa','beta','charlie','delta','beta']
# # b='echo', 'foxtrot','gold'
# # c=['hotel','india','juliette']
# # print(int(a.index('beta'))+1)
# # print(a.count("beta"))
# # a.append(b)
# # print(a)
# # print

# # deret = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 100, 10, 11, 11, 11]

# # print("\nakses list per indeks: ")
# # print(deret[1])
# # print(deret[5])
# # print(deret[10])

# # print("\mencacah isi list: ")
# # for x in deret:
# #     print (x)

# # print("\npanjang list: " + str(len(deret)))

# # print("\nbanyaknya angka 11: " + str(deret.count(11)))

# # print("\nmenambah elemen list dengan append:")

# # deret.append(15)
# # deret.append(16)
# # deret.append(17)
# # deret.append(18)
# # deret.append(19)
# # deret.append(20)
# # deret
# # print(deret)

# # angka=[1,2,3,4,5]
# # angka.append(6)
# # print(angka)


# nama=['abdi','babu','caca','delta','babu']
# #len: menghitung panjang list(int)
# a=len(nama)
# print(a)
# print(type(a))

# #count:menghitung kemunculan nilai tertentu
# print(nama.count('babu'))

# #append(): menambah nilai baru di belakang list.
# nama.append('echo')
# print(nama)

# #index():mencari posisi suatu nilai
# print(nama.index('babu'))

# #insert():menyisipkan suatu nilai ke posisi tertentu
# nama.insert(6,'fanta')
# print(nama)

# #pop() atau remove():membuang nilai tertentu
# nama.pop(3)
# print(nama)

# #extend():menyambung list/ menambahkan list ke dalam list
# nama2=['gani','hendra','arif']
# nama.extend(nama2)
# print(nama)


# #reverse():membalik urutan list
# nama.reverse()
# print(nama)

# #sort():mengurutkan urutan list sesuai abjad
# nama.sort()
# print(nama)

# #max()dan min():mencari nilai max dan min
# angka=[5,3,2,1,6,4]

# # print(max(angka))
# # print(min(nama))

# # #sum():tambah tambahan
# # print(sum(angka))

# print(angka)
# angka.sort()
# print(angka)

# for x in angka:
#     print(x)


# deret=1,2,3,4,5
# deret2=(5,4,3,2,1)
# angka.extend(deret)
# print(angka)  
# angka.extend(deret2)
# print(angka)

# nama[0]='surya'
# print(nama)

# angka=[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, [8, 9]]
# ]

# print(angka[1][1]*angka[0][2])
# print(angka[2][1][0])

# # import math
# # berat=input("masukkan berat badan anda(kg) : ")
# # tinggi=input("masukkan tinggi anda (cm) : ")
# # print()
# # if berat.isdigit() and tinggi.isdigit():
# #     bmi=int(berat)/((int(tinggi)/100)**2)
# #     bmi=round(bmi,1)
# #     if bmi >=30:
# #         print("BMI anda =",bmi,". Anda kegemukan (obesitas).")
# #     elif bmi >=25 and bmi <30:
# #         print("BMI anda =",bmi,". Anda kelebihan berat badan.")
# #     elif bmi>=18.5 and bmi<25:
# #         print("BMI anda =",bmi,". Berat badan anda normal")
# #     else:
# #         print("BMI anda =",bmi,". Berat badan anda kurang.")
# # else:
# #     print("Input yang anda masukkan salah.")

# namaHari={
#     'monday':'senin',
#     'tuesday':'selasa',
#     'wednesday':'rabu'
# }

# print(namaHari['monday'])
# print(namaHari.get('tuesday'))
# print(namaHari.get('friday','maaf data tidak tersedia'))
# namaHari['kamis']='mantap'
# print(namaHari)
# print()
# print(namaHari.keys())
# print(list(namaHari.keys()))
# print()
# print(namaHari.values())
# print(list(namaHari.values()))              #untuk mendapatkan list dari value nya
# print()
# print(namaHari['monday'])
# print(list(namaHari.values()).index('senin'))
# print(list(namaHari.keys())[list(namaHari.values()).index('senin')])
# print(list(namaHari.keys())[0])

#string formatting method di python
x=2000000
print(x)
print('{:,}'.format(x))
print('{:,}'.format(x).replace(',','.'))

print('halo {}, umurmu {}'.format('Andi',27))
print('halo {1}, umurmu {0}'.format('Andi',27))
print('asalmu dari {kota}'.format(kota='Jakarta'))
print('suhu udara = {:f}'.format(25))

y=50000
print('{:,}'.format(y).replace(',','.'))

angka=1
while angka<=10:
    print('angka ke',angka)
    angka+=1