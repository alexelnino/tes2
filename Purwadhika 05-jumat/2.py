import datetime
from datetime import datetime

b = "Jum'at, 12 April 2019"     # Ubah ke datetime!

namaHari = {
    'Monday' : 'Senin',
    'Tuesday' : 'Selasa',
    'Wednesday' : 'Rabu',
    'Thursday' : 'Kamis',
    'Friday' : 'Jum\'at',
    'Saturday' : 'Sabtu',
    'Sunday' : 'Minggu'
}

b = b.replace(',', '').split()

if b[0] in list(namaHari.values()):
    print(b[0])
    b[0] = list(namaHari.keys())[list(namaHari.values()).index(b[0])]
    print(b[0])
else:
    print('Masukkan nama hari yang benar!')

c = ''
for i in range(len(b)):
    c += b[i] + ' '

print(c)
print(type(c))
# Ubah string ke datetime
ubahStrkeDate = datetime.strptime(c, '%A %d %B %Y ')

print(ubahStrkeDate)
print(type(ubahStrkeDate))

print()
