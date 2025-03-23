

# AND OPERATÖRÜ
#sonuc = 10 < x < 20

#True and True => True
#True and False => False
#False and False => False

x = 15
sonuc = (x > 10) and (x < 20)
print(sonuc)

karne_notu = 90
devamsizlik = 3

ssonuc = (karne_notu >= 50) and (devamsizlik < 10)
print(ssonuc)



#OR OPERATÖRÜ (VEYA)
#True or True => True
#True or False => True
#False or False => False

sonuc1 = (x < 10) or (x % 3 == 0)
print(sonuc1)



#NOT OPERATÖRÜ
sonuc2 = not(x > 0)
print(sonuc2)

ceza_bilgisi = False
sonuc3 = (karne_notu >= 85) and (devamsizlik < 10) and (ceza_bilgisi == False)
print(sonuc3)


#IDENTİTY OPERATÖR : is
d = e = [1,2,3,4]
f = [1,2,3,4]

print(d == e)
print(d == f)
print(d is f)
print(d is e)

#MEMBERSHİP OPERATÖR : in
a = ["python", "javascript"]
print("python" in a)
print("python2" in a)

email = "deneme@gmail.com"
print("@" in email)
