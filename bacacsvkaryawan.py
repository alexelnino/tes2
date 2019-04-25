# file=open('karyawan.csv','r')
# print(file.read())

import csv
with open('karyawan.csv','r') as fileku:
    baca=csv.reader(fileku)         #(fileku,delimiter=';')       delimiter untuk menandakan pemisahnya itu titik koma. kalau defaultnya itu harus koma)
    for i in baca:
        print(i)

# #atau
# with open('karyawan.csv','r') as fileku:
#     baca=csv.DictReader(fileku)         #(fileku,delimiter=';')       delimiter untuk menandakan pemisahnya itu titik koma. kalau defaultnya itu harus koma)
#     for i in baca:
#         print(dict(i))

#atau
import csv
myData=[]
with open('karyawan.csv','r') as fileku:
    baca=csv.DictReader(fileku,delimiter=',')         #(fileku,delimiter=';')       delimiter untuk menandakan pemisahnya itu titik koma. kalau defaultnya itu harus koma)
    for i in baca:
        print(dict(i))
        myData.append(dict(i))

#pr=> bikin data dictreader menggunakan reader biasa
#import data csv ke json
