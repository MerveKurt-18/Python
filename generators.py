"""
def sayac(max):
    sayi = 1
    sayilar = []
    while sayi <= max:
        sayilar.append(sayi)
        sayi += 1
    return sayilar

sonuc = sayac(20)
print(sonuc)
"""


# generators u kullanarak bellekte yer kaplamadan sayıları döndürüyoruz.

def sayac(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi += 1

"""
sonuc = sayac(20)
print(next(sonuc))
print(next(sonuc))
print(next(sonuc))
"""

iterator = sayac(20)
#print(next(iterator))

#for i in iterator:
    #print(i)

#sonuc = list(iterator)
#print(sonuc)

liste = (i for i in range(1,11))
print(next(liste))
print(next(liste))
print(next(liste))