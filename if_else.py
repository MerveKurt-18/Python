sayi = -5

if (sayi < 0):
    print("Sayı negatiftir.")
else: 
    print("Sayı pozitiftir.")   



giris = True

if (giris == True):
    print("Merhaba")



username = "Merve"
password = "12345"

if (username == "Merve") and (password == "12345"):
    print("Sisteme giriş yaptınız.")
else:
    print("Girilen bilgiler yanlış")


if (username == "Merve"):
    if (password == "12345"):
        print("Başarıyla giriş yaptınız.")
    else:
        print("parolanız yanlış") 
else:
    print("Kullanıcı adınız yanlış")           

