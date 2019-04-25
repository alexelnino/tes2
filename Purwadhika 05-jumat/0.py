# NESTED LOOP

listku = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

# mengakses list di dalam list

for i in listku:                   # mengakses ketiga baris di dalam list
    for y in i:               # mengakses ketiga elemen di dalam baris
        print(y)

#list di dalam list di dalam list
data = [
    [
        ['Andi', 'Budi', 'Caca'],
        ['Deni', 'Euis', 'Fafa'],
        ['Gigi', 'Hani', 'Inne']
    ],
    [
        ['Janu', 'Koko', 'Lani'],
        ['Momo', 'Nina', 'Opik'],
        ['Peni', 'Qiqi', 'Rogi']
    ],

]

for listku in data:
    for baris in listku:
        for elemen in baris:
            print(elemen)



print()