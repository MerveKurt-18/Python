class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi oluşturuldu.")

    def info(self):
        print(self.name,self.surname,self.age)



class Student(Person):
    def __init__(self,name,surname,age,number):
        super().__init__(name,surname,age)
        self.number= number
        print("student nesnesi oluşturuldu.")

    def ortalama_al(self):
        print(f"{self.number} numaralı öğrencinin ortalaması alındı.")

        

class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("teacher nesnesi oluşturuldu.")

    def teach(self):
        print(f"{self.name} {self.surname} isimli öğretmen {self.branch} eğitimi veriyor.")


p1 = Person("Merve","Kurt",25)
p1.info()

s1 = Student("Şeyma","Koç",20,200)
s1.info()
print(s1.number)
s1.ortalama_al()

t1 = Teacher("Çağla","Şahin",45,"Bilişim Teknolojileri")
t1.info()
t1.teach()
print(t1.branch)