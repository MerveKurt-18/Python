class User:

    # yapıcı metot (constructor)
    def __init__(self, username,name,surname,birthday):
        #object atribute, instance attribute
        self.username = username
        self.name = name
        self.surname = surname
        self.birthday = birthday

    # instance methods
    def info(self):
        return f"{self.username} kullanıcı adıyla {self.name} {self.surname} sisteme kaydedildi."
    def calculateAge(self):
        return f"{self.username} kullanıcısının yaşı :{2025-self.birthday}"

u1 = User("mervek","Merve","Kurt",1999)
u2 = User("merve_k","Merve","Krt",2000)

print(u1.info())
print(u2.info())

print(u1.calculateAge())
print(u2.calculateAge())