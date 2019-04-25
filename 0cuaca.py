import requests
url='https://api.openweathermap.org/data/2.5/weather?q='
namaKota=input('masukkan nama kota : ')
apikey='361fca442399d6dac58d4c36a466273b' 

dataCuaca=requests.get(url+namaKota+'&APPID='+apikey)

cuaca=dataCuaca.json()['weather'][0]['main']
suhu=dataCuaca.json()['main']['temp']
lembap=dataCuaca.json()['main']['humidity']
#print(dataCuaca.json())

print('cuaca=',cuaca)
print('suhu=',round(suhu-273),'*C')
print('kelambapan=',lembap,'%')