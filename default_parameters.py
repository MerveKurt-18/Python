

def selamla(isim="Kullanıcı",mesaj="Hoş geldin"):
    print(f"{mesaj} {isim}")

selamla("Merve","Merhaba")
selamla("Umut")
selamla("Merve","İyi akşamlar")
selamla()


def usAlma(taban,us=2):
    return taban ** us

sonuc = usAlma(4,2)
sonuc = usAlma(4,5)
sonuc = usAlma(3)
print(sonuc)



"""
def carpma(a,b):
    return a * b

def toplama(a,b):
    return a + b

def islem(a,b):
    return carpma(a,b)
sonuc = islem(10,5)
print(sonuc)

veya bunu aşağıda ki gibi de yapabiliriz

"""

def carpma(a,b):
    return a * b

def toplama(a,b):
    return a + b

def islem(a,b,fn):
    return fn(a,b)
sonuc = islem(10,20,toplama) #çarpma istiyorsak çarpma yazacağız toplama istiyorsak toplama.
print(sonuc)