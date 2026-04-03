
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
    
        # Save an task in the day appropry 

    def save (self) :
        if self.day in Task.days :
            Task.days[self.day].append(self.title)

        # Deleted an task 

    def deleted (self) :
        Task.days.pop(self.day)
        print("Task deleted succeful !")            


t1 = Task(title = input("Entrer ta tache  ") , day = "manday")    
t2 = Task(title = "Partir a la fac a 7h15" , day = "manday")    
t5 = Task(title = "Tuesday sport " , day = "tuesday")    
t3 = Task(title = "Partir a la formation" , day = "westerday")    
t4 = Task(title = "Dormir a 23h00'" , day = "friday")  

# print(t1.title)

t1.save()
t2.save()
t3.save()
t4.save()
t5.save()

t1.deleted()
print(Task.days.get("manday"))
t2.deleted()

print(Task.days["manday"])

for cle, valeur in Task.days.items() :
    print(f"La cle : {cle}  et la  valeur {valeur}"  )


 



        