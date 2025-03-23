a = 10
b = 20
c = 30

a, b, c = 10, 20, 30

a, b = b, a # a ile b yer değiştirdi yani a nın değeri 20, b nin değeri 10 oldu.
print(a, b, c)

c += 5 #c = c+5
c -= 5 #c = c-5
c *= 5 #c = c*5
c /= 5 #c = c/5
c **= 5 #c = c**5
c %= 5 #c = c%5
a //= 5 #a = a//5

print(a, b, c)

sayilar = (1,2,3) #sayilar da 3 eleman değil 2 veya 4 eleman olsaydı hata alırdık.
a,b,c = sayilar
print(a, b, c)

sayilar1 = (1,2,3,4,5,6)
a,b,*c = sayilar1 # hata almamak için * işareti ile geri kalan elemanların hepsini c ye veriyoruz
print(a,b,c)

a,*b,c =sayilar1
print(a,b,c)




#comparison(karşılaştırma) operatörleri
x, y, z, d = 10, 10, 20, 5

username = "merve"
password = "123456"

sonuc = (x == y) #x ye ye eşit mi
print(sonuc)

sonuc1 = (x != y) # x y ye eşit değilse
print(sonuc1)

sonuc2 = (x == z) #x eşitse z ye
print(sonuc2)

sonuc3 = (username == "merve")
print(sonuc3)

sonuc4 = (username == "Merve")
print(sonuc4)

sonuc5 = (x > z)
print(sonuc5)

sonuc6 = (x >= y)
print(sonuc6)

sonuc7 = (x < z)
print(sonuc7)

sonuc8 = (x <= z)
print(sonuc8)

sonuc9 = (True == 1)
print(sonuc9)

sonuc0 = (False == 0)
print(sonuc0)

sonucc = (False + True)
print(sonucc)

sonuccc = (False + True + 20)
print(sonuccc)




