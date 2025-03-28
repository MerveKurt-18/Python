
sayilar = [24,5,3,16,72] 

x = sum(sayilar) # listenin içerisindeki elemanları toplar.
print(x)

y = sum(sayilar, 100)
print(y)

urunler = [
    {"title":"kitap a", "price": 25},
    {"title":"kitap b", "price": 35},
    {"title":"kitap c", "price": 45}
]

toplamFiyat = sum([urun["price"] for urun in urunler])
print(toplamFiyat)

a = toplamFiyat / len(urunler)
print(a)

sonuc = round(5.2) #round fonksiyonu yuvarlama işlemi yapar
print(sonuc)
sonucc = round(5.5)
print(sonucc)
soonuc = round(1.343434, 2)
print(soonuc)
ssonuc = round(1.347434, 2)
print(ssonuc)