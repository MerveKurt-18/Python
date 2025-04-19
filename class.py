
# Class
# Class ın isminin ilk harfi büyük olur.

class Arac:
    #method oluşturabiliriz.
    #attribute oluşturabiliriz.
    #Attribute: Bir nesnenin ya da sınıfın sahip olduğu veri/özellik.
    pass


# Instance, Object
arac1 = Arac()
arac2 = Arac()
arac3 = Arac()
class Products:
    pass

p1 = Products() #MacBook Air
p2 = Products() #İphone 13
p3 = Products() #İpad

listProducts = [p1,p2,p3]

for p in listProducts:
    print(p)
    print(type(p))