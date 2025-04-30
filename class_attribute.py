
class User:

    active_users = 0

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
    

print(f"Aktif kullanıcı sayısı: {User.active_users}") 
user1 = User("m_kurt","Merve","Kurt",28)
user2 = User("mervek","Merve1","Kurt1",27)
user3 = User("umut_ü","Umut","Üstün.",29)
print(f"Aktif kullanıcı sayısı: {User.active_users}") 
print(user2.logout())
print(f"Aktif kullanıcı sayısı: {User.active_users}") 