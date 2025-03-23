print(3+1)
print("3"+"3")
print(type(3))
print(type(3.6))
print(type(0.0))
""""
math operatörler
bölmenin sonucu her zaman flout çıkar. 
# ya her satırın başına bunu koyarak yada alta ve üste 3 tane tırnak koyarak yorum satırı yapıyoruz.
ctrl+k+c seçtiğimiz bütün satırları yorum satırı yapar
tekrar yorumdan çıkarmak için ctrl+k ardından ctrl+u yapıyoruz

Değişkenler sayı ile başlayamaz.
urun@ gibi bir kullanım şekli yoktur.
Değişkenler boşluk içeremez.
Türkçe karakter kullanılmamalıdır.
a, b, c = 10, 20, 30 gibi kullanım vardır.
name = "Merve" --) str
isStudent = True --) boolean
"""


#int to float
age = 25
result = float(age)
print(result)

#float to int
weight = 55.6
result = int(weight)
print(result)

#bool to str
isStudent = False
result = str(isStudent)
print(result)

#bool to int
isStudent = False
result = int(isStudent)
print(result)




#STRİNGS
name = "Merve"
surname = "Kurt"
age = "25"
text = "Benim adım " + name + " ve soyadım " + surname +". Yaşım ise " + age + "."
print(text)

password = "abc12345"
print(password[0])
print(password[-1])




#string slicing
print(text[0:5]) # 0.indexten başla 5 e kadar git. 5. yi almıyor.
print(text[6:17])
print(text[:10])
print(text[10:])
print(text[-20:-1])
print(text[0:30:2])
print(text[::2])
print(text[::-1])




#string formats
name1 = "Merve"
surname1 = "Kurt"
age1 = "25"
print("My name is {} {}".format(name1,surname1))
print("My name is {1} {0}".format(name1,surname1))
print("My name is {s} {n}".format(n=name1,s=surname1))
print("My name is {} {}. I`m {} years old.".format(name1,surname1,age1))
print("My name is {0} {1}. I`m {2} years old. {2}".format(name1,surname1,age1))

number = 5/3
print("the result is {n:1.3}".format(n=number))

print(f"My name is {name1} {surname1} and I am {age} years old.")




#string methods
yazi = "Benim adım Merve Kurt. Eskişehir'de yaşıyorum."
sonuc = yazi.upper() #Bütün harfleri büyütür.
print(sonuc) 

sonucc = yazi.lower() #Tüm harfleri küçültür.
print(sonucc)

ssonuc = yazi.title() #Her kelimenin baş harfini büyütür.
print(ssonuc)

soonuc = yazi.capitalize() #Cümlenin ilk harfini büyük yapar.
print(soonuc)

sonnuc = yazi.islower() #Hepsi küçük mü diye soruyoruz.
print(sonnuc)

sonuc1 = yazi.strip() #Başındaki ve sonunda ki boşlukları yok eder.
print(sonuc1)

sonuc2 = yazi.split() #Her kelimeyi ayırıp dizi haline getirir.
print(sonuc2)

sonuc3 = yazi.split(".") #Noktadan ayırıp dizi yaptı.
print(sonuc3)

sonuc4 = "-".join(yazi) #Herbir harfin arasına - koydu.
print(sonuc4)

sonuc5 = " ".join(yazi) #Herbir harfin arasına boşluk koydu.
print(sonuc5)

sonuc6 = yazi.index("Merve") #Bir string içerisinde bir kelime aramak için kullandığımız method.
print(sonuc6)

sonuc7 = yazi.startswith("B") #Neyle başlayıp başlamadığını soruyoruz.
print(sonuc7)
#endswith() komutu da neyle bitip bitmediğini sorgulamak için.

sonuc8 = yazi.replace("Eskişehir","Bursa") #Bir kelimeyi ya da ismi değiştirmek istersek.
print(sonuc8)

sonuc9 = yazi.replace("i","ı").replace("ş","s")
print(sonuc9)