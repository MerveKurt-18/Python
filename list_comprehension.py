
sayilar = []

for i in range(10):
    sayilar.append(i)
print(sayilar)


#expression for item in list
sayilar = [i for i in range(10)]
print(sayilar)

sayilar = [i*2 for i in range(10)]
print(sayilar)

sayilar = [i**i for i in range(10)]
print(sayilar)





liste = [3,8,5,12,40]
sayiilar = [i*2 for i in liste]
sonuc = [str(sayi) for sayi in liste]
print(sonuc)
print(sayiilar)




isim = "Merve"
sonucc = [a.upper() for a in isim]
print(sonucc)



isimler = ["Ayça","Doğa","Kaan","Melis"]
sonuc1 = [x.lower() for x in isimler]
print(sonuc1)
sonuc2 = [y.upper() for y in isimler]
print(sonuc2)