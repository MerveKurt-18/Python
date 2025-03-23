
a = 10
b = 10

if (a > b):
    print("a b den büyük.")
elif (a == b):
    print("a b ye eşit")
else:
    print("b a dan büyük")    



karne_notu = 60

if (karne_notu < 50):
    print("sınıf tekrarı")
elif (karne_notu >= 50) and (karne_notu < 70):
    print("başarılı")
elif (karne_notu >= 70) and (karne_notu < 85):
    print("teşekkür belgesi")
else:
    print("takdir belgesi")    




""""
sayi = int(input("Sayı giriniz: "))

if (sayi > 0):
    if (sayi % 2 == 1):
        print("girilen sayı pozitif tek sayıdır.")
    else:
        print("girilen sayı pozitif çift sayıdır.")    
else:
    print("girilen sayı negatiftir.")

"""






"""
x = int(input("x : "))
y = int(input("y : "))
z = int(input("z : "))

if (x > y) and (x > z):
    print("x en büyük sayı")
elif (y > x) and (y > z):
    print("y en büyük sayı")
elif (z > x) and (z > y):
    print("z en büyük sayı")    
"""







isim = input("isim : ")
yas = int(input("yaş : "))
egitim = input("eğitim : ")

if (yas >= 18):
    if (egitim == "lise" or egitim == "üniversite" ):
        print("ehliyet alabilirsiniz.")
    else:
        print(f'{isim} ehliyet alamazsınız çünkü eğitim durumunuz yetersiz')
else:
    print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor')       

      





