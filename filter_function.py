
yaslar = [7,15,18,27,36]

def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True
    
sonuc = list(filter(yetiskinmi, yaslar))
print(sonuc)    

sonuc1 = list(filter(lambda x: x>=18, yaslar))
print(sonuc1)  

#----------------------


sayilar = [2,5,9,8,12,67]
sonuc2 = list(filter(lambda x: x%2==1, sayilar))
print(sonuc2)

#-----------------------

isimler = ["ali","kemal","sinem","kaan"]
sonuc3 = list(filter(lambda n: n[0]=="k", isimler))
print(sonuc3)
sonuc4 = list(filter(lambda n: n[0]=="y", isimler))
print(sonuc4)

secim = filter(lambda n: n[0]=="k", isimler)
sonucc = list(map(lambda n: n.upper(), secim))
print(sonucc)

sonuuc = list(map(lambda n: n.capitalize(), filter(lambda n: n[0]=="k", isimler)))
print(sonuuc)



#-----------------------

users = [
    {"username" : "leventert", "posts" : []},
    {"username" : "merve", "posts" : ["post1","post2"]},
    {"username" : "merve_kurt", "posts" : ["post1"]}
]

soonuc = list(filter(lambda u: len(u["posts"])>0, users))
print(soonuc)
ssonuc = list(map(lambda u: u["username"].upper(),filter(lambda u: len(u["posts"])>0, users)))
print(ssonuc)
sonuc6 = [user["username"] for user in users if len(user["posts"])>0]
print(sonuc6)

