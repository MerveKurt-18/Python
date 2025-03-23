
def karsilama():
    for i in range(10):
        print("Merhaba")#fonksiyonu çağırmamız gerek çağırmazsak terminalde bir değişiklik olmaz.

karsilama()


a = 5
b = 10

def carpma():
    print(a*b)
    
carpma()


#RETURN
def adin_ne():
    ad = input("Adınızı giriniz: ")
    return ad #return ad yapmazsak printte çıkan none oluyor isim tanımlı olmuyor.

print("Sisteme hoş geldiniz",adin_ne())


def topla():
    return 20+30

sonuc = topla() * 2
print(sonuc)   


saat = 15

def selamla():
    if (saat<12):
        return "Günaydın"
    elif (saat>=12) and (saat<18):
        return "İyi günler"
    else:
        return "İyi akşamlar"

sonucc = selamla() + ", Merve"
print(sonucc)

