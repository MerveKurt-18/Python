
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi oluşturuldu.")

    def info(self):
        print(self.name,self.surname,self.age)

class Student(Person):
    pass

class Teacher(Person):
    pass

p1 = Person("Merve","Kurt",25)
#print(p1.name,p1.surname,p1.age)
p1.info()

s1 = Student("Şeyma","Koç",20)
#print(s1.name,s1.surname,s1.age)
s1.info()

t1 = Teacher("Çağla","Şahin",45)
#print(t1.name,t1.surname,t1.age)
t1.info()