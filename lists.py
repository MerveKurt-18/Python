yazi = "Benim adım Merve Kurt. Eskişehir'de yaşıyorum.".split()
print(yazi)
print(yazi[0])
print(yazi[2][1])

sayilar = [1,2,3,4,5,6]
sonuc = sayilar
sonuc = sayilar[0]
sonuc = sayilar[4]
#sonuc = sayilar[6] 6. index olmadığı için hata aldık.
print(sonuc)

isimler = ["mert","ceyda","kerem","ahmet"]
sonucc = isimler[1]
print(type(isimler))
print(type(isimler[1]))
print(sonucc)

listeMert = ["mert",18]
listeCeyda = ["ceyda",20]
sonuc1 = listeMert[0]
print(sonuc1)

ogrenciler = [["mert",18],["ceyda",20]]
print(ogrenciler)
print(ogrenciler[0])

ogrenciler1 = [listeMert,listeCeyda]
print(ogrenciler1[1])  






#listelerde temel işlemler
iller = ["İstanbul","Ankara","İzmir","Bursa"]
ssonuc = iller
ssonuc = iller[2]
ssonuc = iller[0:2]
ssonuc = iller[2:]
ssonuc = iller[:3]
ssonuc = iller[-3:-1 ]
print(ssonuc)

iller[0] = "Tekirdağ"
iller[-1] = "Balıkesir"
print(iller)

sonuuc = len(iller) #listenin uzunluğu
print(sonuuc)
soonuc = iller + ["Adana","Antalya"] #listeye elaman ekledik
print(soonuc)
del iller[0] #listeden eleman sildik bunu : bunun ile aralık belirterek te yapabilirdik.
print(iller)




#Listelerde metodlar
ssayilar = [100,3,9,14,3,28,36]
harfler = ["v","b","f","k","s","s","a"]

sonuc2 = min(ssayilar) #en küçük eleman için
sonuc2 = max(ssayilar) #en büyük eleman için
print(sonuc2)
sonuc3 = min(harfler) #alfabeye göre sıralamada
sonuc3 = max(harfler)
print(sonuc3)

ssayilar.append(20) #ekleme listenin sonuna ekler
print(ssayilar)
harfler.append("l")
print(harfler)

ssayilar.insert(3,12)#3. indekse 12 yi ekle
print(ssayilar)
harfler.insert(5,"e")
print(harfler)

ssayilar.pop() #listenin sonunda ki elemanı siler(20 yi eklemiştik onu sildi)
print(ssayilar)
harfler.pop() #l harfini sildi
print(harfler)

ssayilar.remove(14) #listeden silmek istediğimiz elemanı siliyoruz.
print(ssayilar)
harfler.remove("f")
print(harfler)

ssayilar.sort() #buradaki sayıları küçükten büyüğe sıralayacak.
print(ssayilar)
harfler.sort()
print(harfler)

ssayilar.reverse() #sayıları büyükten küçüğe sıralar.
print(ssayilar)
harfler.reverse()
print(harfler)

print(ssayilar.count(3)) #listede kaç tane 3 var diye soruyor
print(harfler.count("s"))

print(ssayilar.index(9)) #9 sayısının listede kaçıncı indexte olduğunu yazar.
print(harfler.index("k"))

ssayilar.clear() #listenin içinde ki bütün elemanları siler.
print(ssayilar)
harfler.clear()
print(harfler)
