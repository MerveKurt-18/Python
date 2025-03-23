# list
# tuple
# dictionary
# sets ---> sıralama gerçekleştiremiyoruz[indexlenemez] ve değerleri değiştiremiyoruz.

markalar = {"Audi", "Mercedes","Bmw","Honda"}
markalar2 = {"Renault","Toyota","Mazda"}
# sorgulama
sonuc = "Bmw" in markalar
print(sonuc)

#ekleme yapabiliyoruz.
markalar.add("Opel")
markalar.update(["Toyota","Scoda"]) #Birden fazla eleman eklemek istediğimizde
print(markalar)

sonucc = len(markalar)
print(sonucc)

markalar.remove("Opel") #eleman silmek için
print(markalar)

sonuccc = markalar.pop() #rastgele herhangi bir elemanı siler
print(sonuccc)

#markalar.clear() #listenin içerisini tamamen siler
#print(markalar)

ssonuc = markalar.union(markalar2)
print(ssonuc)