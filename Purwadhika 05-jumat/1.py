import datetime

# x = datetime.datetime.now()         # ngambil waktu lokal komputer masing2

# print(x)                    # type nya datetime
# print(x.year)               # dapet tahunnya aja
# print(x.month)              # bulan bentuknya integer 
# print(x.strftime('%m'))     # bulan tapi angka
# print(x.strftime('%B'))     # bulan tapi huruf
# print(x.strftime('%A'))     # hari tapi namanya in english
# print(x.strftime('%d'))     # tanggal
# print(x.day)                # tanggal
# print(x.strftime('%y'))     # year (2 digit), kalau 4 digit %Y

# print(x.strftime('%H'))     # jam 24h
# print(x.strftime('%I'))     # jam 12h
# print(x.strftime('%M'))     # menit
# print(x.strftime('%S'))     # detik 

# print(x.strftime('%c'))     # tanggal dan waktu tp formatnya beda
# print(x.strftime('%x'))     # tanggal lengkap dengan type nya sudah dalam bentuk string
# print(x.strftime('%X'))     # jam lengkap

# print()
# tanggal = '02/04/2019'       # masih sebagai tipe string
# mau diubah jadi datetime
# ubahStrkeDate = datetime.datetime.strptime(tanggal)         # ada function datetime di dalam library datetime
# strptime: dari string ubah ke object date
# strftime: dari date time diubah ke string


# atau bisa aja
from datetime import datetime
x = '12/12/2019' 
ubahStrkeDateX = datetime.strptime(x, '%d/%m/%Y')                # variabel kedua di dalam kurung utk menentukan format tanggalan kita    
print(ubahStrkeDateX)
print(type(ubahStrkeDateX))


y = '12 Apr 2019'           
ubahStrkeDateY = datetime.strptime(y, '%d %b %Y')              # format bulan dalam alfabet yg disingkat adalah %b, kalau ga disingkat %B
print(ubahStrkeDateY)
print(type(ubahStrkeDateY))

z = '12-04-19 21.45'
ubahStrkeDateZ = datetime.strptime(z, '%d-%m-%y %H.%M')
print(ubahStrkeDateZ)
print(type(ubahStrkeDateZ))

a = 'Friday, 12 April 2019'
ubahStrkeDateA = datetime.strptime(a, '%A, %d %B %Y')
print(ubahStrkeDateA)               # ke print tapi ga dapet harinya
print(type(ubahStrkeDateA))
print(ubahStrkeDateA.strftime('%A'))  # buat ngambil nama harinya --> soalnya formatnya sama dengan datetime.now()



print()