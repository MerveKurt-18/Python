
def userInfo(*args):
    print(type(args))

userInfo()

def userInfo(**kwargs):
    print(type(kwargs))

userInfo()


def userInfo(**kwargs):
    print(kwargs)

userInfo(username="merve")
userInfo(username="merve",password="123456",email="mervekurt@gmail.com")




def userInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        print("\n")
    


userInfo(username="merve",password="123456",email="mervekurt@gmail.com")



def siralama(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(*kwargs)

siralama(1,2,3,4,5,6,key1="value1",key2="value2")
