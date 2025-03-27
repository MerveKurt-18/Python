
sayilar = [2,67,24,47,88,11,8]

#sayilar.sort() => Bunu yaptığımızda sayılar listemiz değişiyor artık bunun sıralamasına göre oluyordu.

sonuc = sorted(sayilar) # Bunu yaptığımızda sayilar listesi değişmiyor yani ilk halini koruyor.
print(sonuc)

ssonuc = sorted(sayilar, reverse=True)
print(ssonuc)

soonuc = sorted((2,67,24,47,88,11,8)) #içerisine tuple gönderdik ve listeye çevirdi
print(soonuc)


users = [
    {"username":"merve", "posts":["post1","post2"], "email":"merve@gmail.com"},
    {"username":"mervekurt", "posts":[]},
    {"username":"m_kurt", "posts":["post1"], "password":"", "phone":"15463458"}
]

a = sorted(users, key=len) #paylaşımı azdan çok olana doğru sıraladı
a = sorted(users, key=len, reverse=True) #paylaşımı çoktan aza doğru sıraladı
a = sorted(users, key=lambda user: user["username"])#alfabetik sıraladı
a = sorted(users, key=lambda user: len(user["posts"]))#post sayısını azdan çok olana doğru sıraladı
print(a)

araclar = [
    {"title":"Audi A4", "price":400000},
    {"title":"Mercedes E", "price":900000},
    {"title":"BMW520", "price":700000}
]

b = sorted(araclar, key=lambda arac: arac["price"])#araç değeri en düşükten en yükseğe doğru sıraladı
b = sorted(araclar, key=lambda arac: arac["price"], reverse=True)#araç değeri en yüksekten en düşüğe doğru
b = list(map(lambda arac: arac["title"], sorted(araclar, key=lambda arac: arac["price"], reverse=True)))#fiyatına göre araçların adını sıraladık


print(b)

