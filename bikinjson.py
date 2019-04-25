import json
x={
    'id':2,
    'kota':'medan'
}

x2=json.dumps(x)
jsonku=open('medan.json','w')
jsonku.write(x2)

#setelah di run maka akan terbentuk file medan.json. untuk mempercantik tampilan di file json, tekan ctrl +shift + p.
#lalu ketik prettify