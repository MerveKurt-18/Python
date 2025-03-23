
sayilar = [1,3,5,8,12]
sayilar1 = ["1","3","5","8","12"]

kareleri = []

for sayi in sayilar:
    kareleri.append(sayi ** 2)

print(kareleri)   


# Bunu map fonksiyonu ile yapalım.

def kareAl(sayi):
    return sayi ** 2

sonuc = list(map(kareAl, sayilar))
print(sonuc)

# Veya bunu lambda fonksiyonu kullanarak ta yapabiliriz.
sonuc1 = list(map(lambda sayi: sayi ** 2, sayilar))
print(sonuc1)

sonuc2 = list(map(int, sayilar1))
print(sonuc2)

sayilar2 = [-1,3,5,-8,-12]
sonuc3 = list(map(abs, sayilar2))
print(sonuc3)

sonuc4 = list(map(float, sayilar))
print(sonuc4)

isimler = ["ayça","yağmur","kemal","tolga"]
sonuc5 = list(map(str.capitalize, isimler))
print(sonuc5)

sonuc6 = list(map(str.upper, isimler))
print(sonuc6)

sonuc7 = list(map(len, isimler))
print(sonuc7)


kullanıcilar = [
    {"ad": "yağmur", "soyad": "yalçın"},
    {"ad": "kemal", "soyad": "solmaz"}
]

soonuc = list(map(lambda x: x["ad"],kullanıcilar))
print(soonuc)

soonuc1 = list(map(lambda x: x["soyad"],kullanıcilar))
print(soonuc1)