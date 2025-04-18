
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



sonuc = os.listdir()
print(sonuc) #---> Python dosyamızdaki klasörleri listeledik
"""
#Listeleme
sonuc = os.listdir("C:\\) ---> C nin içerisindekileri listeledik

"""