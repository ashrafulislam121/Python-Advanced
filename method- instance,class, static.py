class Human:
    def __init__(self, name):
        self.name = name
     
    #Instance method ==> works with object
    def show_name(self):
        print(self.name)
        
    #Class method ===> works with Class    
    @classmethod
    def cls_method(cls):
        print("this is a class method")
        
    #Static method without param ==> works with both
    @staticmethod
    def emnitei():
        print("emnitei print korlam")
        

# Method call by object
human = Human("Nobita")
human.cls_method()

# Also method call by class wtihout creating object
Human.cls_method()

# method call without object as param
human.emnitei()
Human.emnitei() #class can call static method