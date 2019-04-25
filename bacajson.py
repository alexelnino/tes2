# #file json
# #harus tanda petik 2. bentuknya list, terakhir tidak boleh ada koma. kalau angka tidak perlu pakai tanda petik

# import json

# #convert dict => json
# x={
#     'nama':'andi',
#     'usia':23
# }
# x2=['andi','budi']
# y=json.dumps(x)
# y2=json.dumps(x2)

# z1='aku string biasa'
# z2=json.dumps(z1)

# print(x)
# print(y)
# print(x2)
# print(y2)
# print(z2)

# #json =>python
# import json

# x='{"nama":"andi"}'
# y=json.loads(x)
# x2='["andi","budi","caca"]'
# y2=json.loads(x2)
# print(x)
# print(y)
# print(x2)
# print(y2)

import json
with open('data.json') as dataku:
    data=json.load(dataku)

print(data)
print(type(data))
print(data[0]['nama'])