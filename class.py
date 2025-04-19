
# Class
# Class ın isminin illk harfi büyük olur.

class Arac:
    #method oluşturabiliriz.
    #attribute oluşturabiliriz.
    pass


# Instance, Object
arac1 = Arac()
arac2 = Arac()

class Products:
    pass

p1 = Products() #MacBook Air
p2 = Products() #İphone 13
p3 = Products() #İpad

listProducts = [p1,p2,p3]

for p in listProducts:
    print(p)
    print(type(p))