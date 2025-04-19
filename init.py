"""
class Product:
    def __init__(self):
        self.name = "Mercedes A"
        self.price = "600000"
        print("product nesnesi oluşturuldu")

p1 = Product()
p2 = Product()

print(p1.name,p1.price)
print(p2.name,p2.price)

Böyle yaptığımızda iki nesne içinde aynı name aynı price oluyor. Biz buraya ne kadar nesne eklersek ekleyelim hepsi aynı olacak.

"""

class Product:
    def __init__(self, name, price, isActive=True):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product nesnesi oluşturuldu")

p1 = Product("Mercedes A", "600000")
p2 = Product("BMW 320", "500000", False)
p3 = Product("Opel Astra", "300000")

print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)
print(p3.name,p3.price,p3.isActive)
