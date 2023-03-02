class Human:
    
    #class variable
    cls_v = "class variable"
    
    def __init__(self, name):
        #instance variable
        self.name = name
     
    
    def show_name(self):
        print(self.name) #instance variable only can be accessed by instant method
        print(cls.cls_v) #class variable accessed by instant method
        
   
    @classmethod
    def cls_method(cls):
        print(cls.cls_v) #class variable accessed by class method
                        #instance variable can't be accessed by class method
        
  
    @staticmethod
    def emnitei():
        print("emnitei print korlam") #class variable & instance variable cann't be accessed by static class
        

# Method call by object
human = Human("Nobita")
human.cls_method()

# Also method call by class wtihout creating object
Human.cls_method()

# method call without object as param
human.emnitei()
Human.emnitei() #class can call static method
