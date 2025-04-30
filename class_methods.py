class User:

    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane aktif kullanıcı var."
    

    @classmethod
    def from_string(cls,data_str):
        username,name,surname,age = data_str.split(",")
        return cls(username,name,surname,age)


    def __init__(self,username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1


    def userName(self):
        return f"{self.username}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.username} programdan çıkış yaptı."
    

print(User.display_active_users()) 
#user1 = User("m_kurt","Merve","Kurt",28)
#user2 = User("mervek","Merve1","Kurt1",27)
#user3 = User("umut_ü","Umut","Üstün.",29)

user5 = User.from_string("Esra_krt,Esra,Kurt,20")
print(User.display_active_users())
print(user5.username)
print(user5.name)
print(user5.surname)