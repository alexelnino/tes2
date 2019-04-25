# # deret = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 100, 10, 11, 11, 11]
# # print(deret)
# # print("\nakses list per indeks: ")
# # print(deret[1])
# # print(deret[5])
# # print(deret[10])

# # print("\nmencacah isi list: ")
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
# # print(deret)

# # print("\nmencari indeks suatu nilai dengan index: ")

# # print(deret.index(100))
# # print(deret.index(15))
# # print(deret.index(10))
# # print(deret.index(17))

# # print("\nmenambah elemen list dengan insert:")

# # deret.insert(2, 35)
# # deret.insert(2, 36)
# # deret.insert(2, 37)
# # deret.insert(2, 38)
# # deret.insert(2, 39)
# # deret.insert(2, 30)
# # print(deret)

# # print("\nmembuang elemen list dengan pop:")

# # deret.pop()
# # deret.pop()
# # deret.pop()
# # print(deret)

# # print("\nmembuang elemen list dengan remove:")

# # deret.remove(35)
# # deret.remove(36)
# # deret.remove(37)
# # deret.remove(38)
# # deret.remove(39)
# # deret.remove(30)
# # print(deret)

# # print("\nmenambah elemen list dengan extend:")

# # deret2 = [1, 2, 3, 4, 5]
# # deret.extend(deret2)

# # print(deret)

# # print("\nmembalik list dengan reverse:")
# # deret.reverse()
# # print(deret)

# # print("\nmengurut list dengan sort:")
# # deret.sort()
# # print(deret)

# #looping #1
# angka=1
# while angka<=10:
#     print('haha ke-',angka)
#     angka+=1
# print()
# angka=[11,22,23,24,25,26,27]
# angka2=[]
# print(len(angka))
# i=0
# while i<=len(angka)-1:
#     print(angka[i]*2)
#     i+=1

# print(angka)
# print(angka2)
# print()

# i=0
# while i<=6:
#     print(i)
#     if i==4:
#         break
#     i+=1
# print()
i=0
# while i<=6:
#     i+=1
#     if i==4:
#         continue
#     print(i)

# for data in range(0,11):
#     print('haha ke-',data)

angka=[1,2,3,4,5,6]
# i=0
# while i<=len(angka)-1:
#     print(angka[i]*2)
#     i+=1

# i=0
# while i<10:
#     i+=1
#     if i==4:
#         continue
#     print(i)

for i in range(len(angka)):
    print(angka[i])
print()
for i in angka:
    print(i)

#membuat bintang
star=''
for i in range(7):
    star+=' * '
    print(star)

angka=''
for i in range(5):
    angka=angka+str(i)+' '
for i in range(5):
    for j in range(5):
        print(i,'dan',j)

#cara membuat segitiga dengan menggunakan input angka
# star=""
# for i in range (5):
#         star+="*"
#         print(star)

# x=int(input("masukkan angka : "))
# bar=1
# no=1
# string=""
# while bar<=x:
#         kol=bar
#         while kol>0:
#                 string=string+" "+str(no)+" "
#                 kol=kol-1

#         string=string+"\n"
#         bar=bar+1
#         no=no+1
# print(string)

# string=""
# bar=1
# no=1
# x=int(input("masukkan angka : "))
# while bar<=x:
#         kol=bar
#         while kol>0:
#                 string=string+" "+str(no)+" "
#                 kol=kol-1
#         string=string+"\n"
#         bar=bar+1
#         no=no+1
# print(string)

string = ""
bar = 1

x = int(input("Masukkan angka :"))

# Looping Baris
while bar <= x:
	kol = bar

	# Looping Kolom
	while kol > 0:
		string = string + " * "
		kol = kol - 1
		
	string = string + "\n"
	bar = bar + 1
print (string)
