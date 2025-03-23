
def us_alma(a):
    return a ** 2

print(us_alma(3))

#Bunu lambda fonksiyonunu kullanarak yapalım.
# lambda arguments : expression

sonuc = (lambda a: a ** 2)(4)
print(sonuc)



us_almaa = (lambda a: a **2)
sonuc = us_almaa(6)
print(sonuc)


toplama = lambda a,b,c: a+b+c
sonucc = toplama(5,8,12)
print(sonucc)


tersCevir = lambda x: x[::-1]
ssonuc = tersCevir("Merve Kurt")
print(ssonuc)


def fn1(n):
    return lambda a: a ** n

us_alma2 = fn1(2)

soonuc = us_alma2(7)
print(soonuc)