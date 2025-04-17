def users(username,city):
    citys = ["istanbul","ankara","izmir","antalya","bursa","eskişehir"]
    if type(username) is not str:
        raise TypeError("username str tipinde olmalıdır.")
    if type(city) is not str:
        raise TypeError("city str tipinde olmalıdır.")
    if city not in citys:
        raise ValueError("geçersiz bir şehir girdiniz.")
    

try:
    users("merve","eskişehir")
except Exception as e:
    print(e)
else:
    print("Bilgiler başarıyla girildi")

# Hata fırlatma: istemediğimiz bir durum gerçekleştiğinde hata almak. bunu da raise komutuyla yapıyoruz.

#olabilecek hataları denemek için yapıyoruz..

#test commit