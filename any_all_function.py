# Bize boolean değer döndüren fonksiyonlar

x = all([True,False,True])
print(x) #Listenin içinde tek bir False olması all fonkiyonuyla çalıştırdığımızda hepsi True değilse sonucun False çıkmasını sağlar.

a = all([True,True,True])
print(a)


b = any([False,False,True])
print(b) #any fonksiyonunda tek bir True olması çıktı da True dönmesini sağlar.

c = any([False,False,False])
print(c)

# True and True = True => All()
# True and False = True => Any()


sayilar = [0,1,4,7,8,10,15]
sonuc = [bool(sayi) for sayi in sayilar]
print(sonuc)

y = any([bool(sayi) for sayi in sayilar])
print(y)

z = all([bool(sayi) for sayi in sayilar])
print(z)

s = all([bool(sayi) for sayi in sayilar if sayi%2==1])
print(s)

v = all([sayi%2==0 for sayi in sayilar])#Hepsi çift sayı mı diye soruyoruz
print(v)

k = any([sayi%2==0 for sayi in sayilar])#Herhangi biri çift sayı mı diye soruyoruz
print(k)


isimler = ["ali","arda","mehmet","didem"]
sonucc = [isim[0]=="a" for isim in isimler]
print(sonucc)

ssonuc = any([isim[0]=="a" for isim in isimler])#isimler listesinde ismi a ile başlayan en az bir kişi var mı
print(ssonuc)

soonuc = all([isim[0]=="a" for isim in isimler])#isimler listesindeki isimlerin hepsi a ile mi başlıyor
print(soonuc)