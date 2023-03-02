class Robot: 
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
    def show_name(self):
        print(self.name)
    
    def show_age(self):
        print(self.age)
        
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