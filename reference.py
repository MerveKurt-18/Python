# value types => string, number:
# üzerinde değişiklik yaptıktan sonra önceki bundan etkilenmemiş oluyor.
sayi1 = 10
sayi2 = 20

sayi1 = sayi2
sayi2 = 30
print(sayi1,sayi2)


# referance types => lists
x = ["python","javascript"]
y = ["python","javascript"]

x = y
y[0] = "html"
print(x,y)
