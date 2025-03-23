
a = 10
b = 20

def topla():
    return a + b

sonuc = topla()
print(sonuc)

#VEYA ŞU ŞEKİLDE DE YAPABİLİRİZ:

def toplaa(x,y):
    return x + y

sonucc = toplaa(10,20)#burada istersek farklı sayılarda yazabilirdik.ve bunlara aynı şekilde z değişkeni de ekleyebiliriz.
print(sonucc)



def yasHesapla(dogumYili):
    return 2025 - dogumYili

sonuc1 = yasHesapla(1999)
print(sonuc1)



def selamla(isim):
    return "Merhaba, " + isim

sonuc2 = selamla("Merve")
print(sonuc2)



def kayit_et(ad,soyad,sehir):
    print("Ad     : ",ad)
    print("Soyad  : ",soyad)
    print("Şehir  : ",sehir)
    print("Kişi başarıyla kaydedildi.")

sonuuc = kayit_et("Merve","Kurt","Eskişehir")
print(sonuuc)