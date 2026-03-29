
class Task :
    days = {
     
    "manday" : [],
    "tuesday" : [],
    "westerday":[],
    "friday" : [] 

     }

    def __init__(self,title,day):

        self.title = title
        self.day = day  
    
        # Stocker une tache dans le jour approprie 

    def stocker (self) :
        if self.day in Task.days :
            Task.days[self.day].append(self.title)

        # Supprimer une tache 

    def deleted (self) :
        print("Task deleted succeful !")            


t1 = Task(title = input("Entrer ta tache  ") , day = "lundi")    
t2 = Task(title = "Partir a la fac a 7h15" , day = "lundi")    
t3 = Task(title = "Partir a la formation" , day = "lundi")    
t4 = Task(title = "Dormir a 23h00'" , day = "lundi")  

# print(t1.titre)

t1.stocker()
t2.stocker()
t3.stocker()
t4.stocker()
print(Task.days["manday"])






        