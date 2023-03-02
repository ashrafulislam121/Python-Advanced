#======================================================
#super()
#======================================================

class Robot: 
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
    def show_name(self):
        print(self.name)
    
    def show_age(self):
        print(self.age)

#inheritanced by Robot ==> so human_obj can access Robot's method
class Human():
    def __init__(self, name, age, food):
        #supered by Robot ==> so human_obj  can access Robot's __init__ variable 
        #super().__init__(name,age)
        self.name = name
        self.age = age
        self.food = food
        
    def show_name(self):
            print(self.name)
        
    def show_age(self):
            print(self.age)
            
    def show_food(self):
            print(self.food)
            
            
class Animal(Robot, Human): #==> super() take Animal'sclass and Go to firt_mentioned class
                                #and got an error because there are no foor argument in first_class
    def __init__(self, name,age,food,pet):
        Human.__init__(self,name,age,food) #==> We can solve it by mentioning spacefic Human_class insted of Super()
        #if you this use self must
        self.pet = pet
    
    def show_pet(self):
        print(self.pet)
            
            
robot = Robot("Sophiya", "5 years")
human = Human("shinchan", "3 years", "Apple")
animal = Animal("Shiro", "6 years", "cake", "pet animal")

print("--------Robot----------")
robot.show_name()
robot.show_age()

print("--------Human----------")
human.show_name()
human.show_age()
human.show_food()

print("--------Animal----------")
animal.show_name()
animal.show_age()
animal.show_food()

