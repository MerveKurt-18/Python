#tuples(demetler)
#elemanları değiştirilemeyen listelerdir.

list1 = [1,3,5,13]
thistuple = (1,2,"altı",False,1)
thistuple1 = (1,4,"beş",True,1)

print(type(list1))
print(type(thistuple))

print(list1[0])
print(thistuple[2])

print(len(list1))
print(len(thistuple))

list1[0] = 6
print(list1)
#thistuple[0] = 7 --> hata aldık çünkü tuple içinde ki elemanlar değiştirelemez.
#print(thistuple)

#tuple içine eleman eklenip çıkartılamaz.

print(thistuple.count(1)) # 1 elemanının kaç defa geçtiğine baktık.

print(thistuple + thistuple1) #tuple leri birbirine ekleyebiliriz.

list2 = tuple([6,8,3,12]) # listeyi demete dönüştürdü.
print(type(list2))
print(list2)



#dictionary--> key- value şeklinde oluyor.
plakalar = {"İzmir": 35, "İstanbul": 34}
print(plakalar["İzmir"])
print(plakalar["İstanbul"])

plakalar["Eskişehir"] = 26
plakalar["Bursa"] = 16
print(plakalar)




urunler = {
    100: {
        "urunAdi" : "Monitör",
        "urunAciklamasi" : "16 inç",
        "garantiSuresi" : 3,
        "fiyati" : [800,944],
    },
    101: {
        "urunAdi" : "SSD",
        "urunAciklamasi" : "256 GB",
        "garantiSuresi" : 2,
        "fiyati" : [1500,1770],
    }
}

sonuc = urunler
print(sonuc)
print(type(urunler))

sonucc = urunler[100]
print(sonucc)

sonuc1 = urunler[100]["urunAdi"]
print(sonuc1)

sonuc2 = urunler[101]["fiyati"]
print(sonuc2)

tutar = urunler[100]["fiyati"][1] + urunler[101]["fiyati"][1]
print(tutar)  






# dictionary methods
arabaAudi = {
    "marka" : "Audi",
    "model" : "A5",
    "yil" : 2019,
}

# değerlere erişme
sonuc3 = arabaAudi["marka"]
print(sonuc3) # bunu kod olmadan değere erişebildik. Kod ile de erişebiliriz.
sonuc4 = arabaAudi.get("marka")
print(sonuc4)

# sorgulama işlemleri
sonuc5 = "marka" in arabaAudi
print(sonuc5)

sonuc6 = len(arabaAudi)
print(sonuc6)

# ekleme işlemleri
arabaAudi["renk"] = "siyah"
print(arabaAudi)

# silme işlemleri
arabaAudi.pop("yil")
print(arabaAudi)

# son elemanı silme
arabaAudi.popitem()
print(arabaAudi)

#silmek istenen elemanı seçerek silme
#del arabaAudi["marka"]
print(arabaAudi)

#del arabaAudi ---> arabaAudi iy komple siler(objeyi siler)

#arabaAudi.clear() #---> arabaAudi duruyor içerisindeki elemanlar siliniyor.
#print(arabaAudi)

#objeyi kopyalama
araba = arabaAudi.copy()
print(araba)
araba["model"] = "A3"
print(araba)

# değer güncelleme
arabaAudi.update({
    "marka" : "BMW",
    "renk" : "beyaz",
})
print(arabaAudi)
