
isim = "Merve Kurt"

for harf in isim:
    if(harf == "v"):
        break

    print(harf)



i = 0

while (i<10):
    i += 1
    if (i==5):
        continue
    print(i)
print("döngü bitti")  


# 1-100 arasındaki tek sayıların toplamı
a = 0
toplam = 0

while (a <= 100):
   a += 1
   if (a %2 ==1):
      continue
   toplam += a

print(f'toplam: {toplam}')



"""
liste = [4,8,11,18]

for i in liste:
    print(i)


""" 






"""
r = range(10) #10 sayısına kadar demek yani 10 stop sayısı
r = range(1,10) # bunda da başlangıç 1 bitiş 10
r = range(5,20,2) # 5ten başlasın 20 ye kadar devam etsin 2 şer 2 şer artsın
r = range(0,-30,-2)
r = range(100,0,-5)
sonuc = list(r)
print(sonuc)
"""



"""
for i in range(10):
    print(i)

for x in range(1,20,2):
    print(x)
"""

for i in range(1,100):
    if(i % 2 == 1):
        print(i)
