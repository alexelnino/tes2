import datetime
from datetime import datetime

x = datetime.now()

namaHari = {
    'Monday' : 'Senin',
    'Tuesday' : 'Selasa',
    'Wednesday' : 'Rabu',
    'Thursday' : 'Kamis',
    'Friday' : 'Jum\'at',
    'Saturday' : 'Sabtu',
    'Sunday' : 'Minggu'
}

hariIni = namaHari[x.strftime('%A')]
print(hariIni)

tanggal = x.strftime('%d-%B-%Y')
jam = x.strftime('%H')


print('Sekarang hari', hariIni, 'tanggal', tanggal, 'jam', jam)