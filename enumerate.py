
diller = ["Python","JavaScript","Flutter"]

"""
index = 0
for i in diller:
    print(f"{index+1}-{diller[index]}")
    index += 1
"""


#enumerate metodu
obje = enumerate(diller)

print(type(obje))
print(list(obje))


for i in enumerate(diller):
    print(i)


for index,value in enumerate(diller,1): #1 yazmamızın sebebi index sıfırdan değil 1 den başlasın diye
    print(f"{index}-{value}")
