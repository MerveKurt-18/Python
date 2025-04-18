
import os
#sonuc = dir(os)
s = os.name #windows işletim sistemi kullandığımız için nt yazdı
print(s)


# Etkin Dizin Öğrenme
x = os.getcwd()
print(x)

#Dizin değiştirme
#os.chdir("..") # Bir üst dizine atlar. Tekrar tekrar atlamak istersek("../..") yapabiliriz.
#os.chdir("C:\\") # Direk C dizinine ulaştık.


# Klasör Oluşturma
#os.mkdir("yeniklasor")
#os.mkdir("yeniklasor/deneme")---> yeni klasör içerisinde deneme klasörü oluşturduk.
#os.rename("yeniklasor","ustklasor")--->yeniklasor ismini ustklasor olarak değiştirdik
#os.rmdir("ustklasor")---> içiçe olmayan tek olan klasörü silmek için
#os.removedirs("yeniklasor/deneme")--->içiçe olan klasörü tek seferde silmek için kullanılır

#Listeleme
#sonuc = os.listdir()
#print(sonuc) #---> Python dosyamızdaki klasörleri listeledik
#sonuc = os.listdir("C:\\) ---> C nin içerisindekileri listeledik

#Bütün .py dosyalarını listeledik
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

sonuc = os.stat("errors.py") # errors.py dosyası ile ilgili bilgileri aldık
print(sonuc)
#x = sonuc.st_size/1024 --->errors.py dosyasının ne kadar yer kapladığına baktık.yani boyutuna baktık
#1024 e böldük çünkü kilowatt cinsinden aldık