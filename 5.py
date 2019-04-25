#read.txt file => 'r'
#open()=> access local file

# file=open('5.txt','r')          #'r' => command untuk membaca file

# print(file.readable())          #readable untuk memeriksa apakah file txt nya bisa kebaca atau tidak
# print(file.read())              #membaca file

# if file.readable():
#     print(file.read())
#     print(file.readlines())
# else:
#     print('maaf file anda tidak bisa dibaca')

# if file.readable():
#     print(file.read())
#     myList=file.readlines()
#     print(myList[0])
#     for x in myList:
#         print(x)
# else:
#     print('maaf file anda tidak bisa dibaca')

#open()=>access local file
#'r'=>read
#'w'=>write new file/overwrite. file ny bisa macam2 .docx .py .mpeg
#'a'=>append file

# file=open('5.txt','w')
# file.write('selamat pagi!')

# file=open('6.py','w')
# file.write('print(\'Halo\')')

# file=open('6.js','w')
# file.write('console.log(\'Halo\')')

# file=open('6.py','w')
# file.write('print(\'Halo 1\')\n')
# file.write('print(\'Halo 2\')')

# #yang ke print cuma halo 2
# file=open('6.py','w')
# file.write('print(\'Halo 1\')\n')

# file=open('6.py','w')
# file.write('print(\'Halo 2\')\n')

# #yang keprint halo 1 dan halo 2
# file=open('6.py','w')
# file.write('print(\'Halo 1\')\n')

# file=open('6.py','a')
# file.write('print(\'Halo 2\')\n')

#memasukkan list ke dalam file .txt
list=['andi','budi','caca']

file=open('6.txt','w')

for x in list:
    file.write('\n'+x)
