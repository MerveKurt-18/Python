
def toplama(a,b):
    return a + b
def cikarma(a,b):
    return a - b
def carpma(a,b):
    return a * b
def bolme(a,b):
    return a / b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(4,5))
    elif islem_adi == "cikarma":
        print(f2(10,4))
    elif islem_adi == "carpma":
        print(f3(3,7))
    elif islem_adi == "bolme":
        print(f4(20,4))
    else:
        print("geçersiz işlem")

islem(toplama,cikarma,carpma,bolme, "toplama")
islem(toplama,cikarma,carpma,bolme, "cikarma")
islem(toplama,cikarma,carpma,bolme, "carpma")
islem(toplama,cikarma,carpma,bolme, "bolme")
islem(toplama,cikarma,carpma,bolme, "bolme2")