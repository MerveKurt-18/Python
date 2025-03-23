
sayilar = [1,3,6,8,12,16]

for i in sayilar:
    print(i)

for i in sayilar:
    print("Merhaba")


isimler = ["sinem","barış","mert","deniz"]

for isim in isimler:
    print(isim)



iisim = "Merve Kurt"

for i in iisim:
    print(i)



_tuple = [(1,2),(3,4),(6,9)]  

for a,b in _tuple:
    print(a,b)



iller = {"01":"Ankara","02":"Adıyaman","03":"Afyon","04":"Ağrı"}

for x in iller:
    print(x)

for x in iller:
    print(iller[x])

for y in iller.values():
    print(y)

for key,value in iller.items():
    print(key,value)
