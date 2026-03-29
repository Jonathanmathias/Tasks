from users import User

class Admin(User):
        def __init__(self, name, email, password, age, pays):
                super().__init__(name, email, password, age, pays)

        def del_user(self,email) :
                for user in User.users :
                    if user.email == email :
                            User.users.remove(user)
                        
                            print(f"Deleted ")


                if user.email == self.email :
                       print(f"Tu ne peux pas supprimeer {self.name} car c'est un admin !" )

                else :
                    print("L'utilisateur non trouver !")
                        

admin = Admin("Mathias","mathias@gmail.com",123,23,"Burundi")
admin.register()

u5 = User("jojo","Jon@12gmail.com","123",23,"Burundi")
print(u5.name)
admin.del_user("Jon@12gmail.com")
print(User.users)