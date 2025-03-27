
sayilar = [1,7,3,52,28,93,34]
harfler = ["b","a","v","k","d"]
isimler = ["ali","sercan","didem","eray","ahmet"]

a = min(sayilar)
print(a)
b = max(sayilar)
print(b)

x = min(harfler)
print(x)
y = max(harfler)
print(y)

c = min(isimler)
print(c)
d = max(isimler)
print(d)

sonuc = [len(isim) for isim in isimler]
print(sonuc)
ssonuc = min([len(isim) for isim in isimler])
print(ssonuc)
ssoonuc = max([len(isim) for isim in isimler])
print(ssoonuc)

soonuc = max(isimler, key=lambda n: len(n))
print(soonuc)
sonucc = min(isimler, key=lambda n: len(n))
print(sonucc)


araclar = [
    {"title":"Audi A4", "price":500000},
    {"title":"Mercedes E", "price":900000},
    {"title":"BMW 520", "price":800000}
]


son = min(araclar, key=lambda urun: urun["price"])
print(son)
soon = max(araclar, key=lambda urun: urun["price"])
print(soon)
sonn = max(araclar, key=lambda urun: urun["price"])["title"]
print(sonn)

max = 0
for urun in araclar:
    if urun["price"]>max:
        max = urun["price"]

print(max)