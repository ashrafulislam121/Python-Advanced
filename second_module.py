from first_module import Human

class Animal(Human): #==> super() take Animal'sclass and Go to firt_mentioned class
                                #and got an error because there are no foor argument in first_class
    def __init__(self, name,age,food,pet):
        Human.__init__(self,name,age,food) #==> We can solve it by mentioning spacefic Human_class insted of Super()
        #if you this use self must
        self.pet = pet
    
    def show_pet(self):
        print(self.pet)