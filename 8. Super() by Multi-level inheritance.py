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
class Human(Robot):
    def __init__(self, name, age, food):
        #supered by Robot ==> so human_obj  can access Robot's __init__ variable 
        super().__init__(name,age)
        # self.name = name
        # self.age = age
        self.food = food
        
    # def show_name(self):
    #         print(self.name)
        
    # def show_age(self):
    #         print(self.age)
            
    def show_food(self):
            print(self.food)
            
            
robot = Robot("Sophiya", "5 years")
human = Human("shinchan", "3 years", "Apple")

print("--------Robot----------")
robot.show_name()
robot.show_age()

print("--------Human----------")
human.show_name()
human.show_age()
human.show_food()

