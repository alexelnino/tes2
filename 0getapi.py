#get API https://jsonplaceholder.typicode.com/users

#package untuk import url. import request

import requests
namaKlub=input('ketik nama klub :')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+namaKlub

players=requests.get(url)

for player in players.json()['player']:
    print(player['strPlayer'],'(',player['strNationality'],')')


nama=input('ketik nama pemain : ')
url = 'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t='+nama

players=requests.get(url)

for player in players.json()['player']:
    print(player['strTeam'])



