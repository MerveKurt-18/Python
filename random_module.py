
import random
s = dir(random) # random modulünün içerisindeki metotların hepsini gösterir
print(s)

sonuc = random.random() # 0.0-1.0
print(sonuc)
sonuc1 = random.random() * 10
print(sonuc1)
sonuc2 = random.uniform(10,100)
print(sonuc2)
sonuc3 = random.uniform(10,100)
print(sonuc3)
sonuc4 = int(random.uniform(10,100))
print(sonuc4)
sonuc5 = random.randint(1,100)
print(sonuc5)

users = ["mehmet","selin","kaan","cenk","ege"]

sonuc6 = users[random.randint(0,len(users)-1)] # Bunu kısa olarak aşağıdaki gibi yapabiliriz.
print(sonuc6)
sonuc7 = random.choice(users)
print(sonuc7)

isim = "Merve"
sonuc8 = random.choice(isim)
print(sonuc8)

liste = list(range(10))
random.shuffle(liste) #liste elemanlarını karıştırır.
print(liste)

liste1 =range(100)
sonuc9 = random.sample(liste1, 3)
print(sonuc9)

sonuc10 = random.sample(users, 2)
print(sonuc10)