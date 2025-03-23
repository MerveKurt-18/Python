#global scope(alan)
a = "global değer"

def fn1():
    #local değer
    a = "local değer" #yani sadece fonksiyon içinde a bnın bu değeri geçerli
    print(a)
fn1()
print(a)



#-------------------------------------------------


"""
#global
city = "İstanbul"

def changeCity(new_city):
    #local
    city = new_city
    print(city)

changeCity("Bursa")
print(city)

"""


#-------------------------------------------------


"""
city = "İstanbul"

def dis_fonksiyon():
    city = "İzmir"

    def ic_fonksiyon():
        city = "Ankara"
        print("iç fonksiyon " + city)

    ic_fonksiyon()
    print(city)

dis_fonksiyon()
print(city)

"""

#-------------------------------------------------
a = 10

def fn2():
    global a

    print(f"a : {a}")

    a = 20
    print(f"changed a to {a}")

fn2()
print(a)
