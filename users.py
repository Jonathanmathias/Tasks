
class User :
    users = []

    def __init__(self,name, email, password ,age,pays):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.pays = pays
        User.users.append(self)
    def register (self) :
        print(f"L'enregistrement de Mr {self.name} est avec succes)")
            
    def login (self, email, password) :
 
        if self.email == email and self.password == password :
            print(f"Connexion de {self.name} reussie !")

        else  :
            print("Email ou mot de passe incorect !")


u1 = User(name = "Jonathan", email = "jonathanmathias889@gmail.com", password = "Jon123",age=23, pays= "Burundi") 
u1.register()         
u4 = User("Jon","Jon@12ggmail.com",123,23, "Burundi")
u4.register()





