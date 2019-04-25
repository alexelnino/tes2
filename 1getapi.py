import requests
bank=input('masukkan nama bank : ')
url='https://kurs.web.id/api/v1/'+bank

kurs=requests.get(url)
for x in kurs.json()['x']:
    print(x['jual'],'(',x['beli'],'),')
