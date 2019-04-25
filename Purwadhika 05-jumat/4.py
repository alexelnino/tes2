# Anonymous function --> LAMBDA function

# def x(a):
#     return a
# print(x(5))

# y = lambda a : a       # a pertama adalah parameter, setelah titik 2 adalah nilai returnya
# print(y(22))        # ngeprint 22

# z = lambda a : a * 2        # polanya mirip sama return
# print(z(4))

# print()

# def x(a,b,c):
    # return a+b+c

# y = lambda a,b,c : a+b+c        # ini jadinnya kayak return function yang biasa

# print(x(1,2,3))
# print(y(4,5,6))

# y = lambda a,b,c : print(a+b+c)     # kalau ini jadinya kayak function yang biasa
# print(y(4,5,6))

# print() 

def kali(n):
    return lambda x : x * n         # lambda sendiri merupakan suatu function yang merupakan hasil return dari function KALI, dimana x merupakan parameter lambdanya dan x*n merupakan return valuenya

kaliDua = kali(2)       # ini merupakan fungsi lambdanya
kaliTiga = kali(3)

print(kaliDua(26))
print(kaliTiga(33))

print()

# # kalau misalkan tanpa lambda function, maka harus bikin 2 function seperti ini:

def y(a):
    return a

def x(a):
    print(y(a))

x(12)

# jadi kalau ditulis dalam bentuk lambda function:
def z():
    return lambda a : a
b = z()
print(b(13))

print()    