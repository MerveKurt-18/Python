"""
# Bu yaptığımız işlemin adı kapsülleme (encapsulation)
def dis_fonksiyon(sayi1):
    print("dış fonksiyon çalıştı.")
    def ic_fonksiyon(sayi1):
        print("iç fonksiyon çalıştı")
        return sayi1 **2
    sayi2 = ic_fonksiyon(sayi1)
    print(sayi1, sayi2)
dis_fonksiyon(5)
"""


def faktoriyel(number):
    if not isinstance(number, int):
        raise TypeError("Girdiğiniz veri tam sayı omalıdır.")
    if not number >=0:
        raise ValueError("Girdiğiniz sayı sıfırdan büyük olmalıdır.")
    def ic_faktoriyel(number):
        if number <= 1:
            return 1
        return number * ic_faktoriyel(number - 1)
    return ic_faktoriyel(number)

try:        
    print(faktoriyel(-5))
except Exception as e:
    print(e)



