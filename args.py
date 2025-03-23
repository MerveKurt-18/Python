"""
numbers = [5,15,20,25]

def topla(sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc += i
    return f"Sayıların toplamı: {sonuc}"

print(topla(numbers))
"""

#Bunun yerine daha kolay *args ile yapılan yöntemimiz var.

def topla(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(topla(5,20,40,60))
print(topla(5,20,40,60,70))