class Doremon:
    def doremon_self (self):
        print("I am Doremon. I come from the future")
    
    def gadget(self):
        print("New Gadget.", end="\n \n")
    
    
class Nobita: #Nobita_class is inharited by Doremon_class
    def nobita_self(self):
        print("I am Nobita. My hobby is sleep", end="\n\n")
        
class Shizuka(Doremon, Nobita):
    def shizuka_self(self):
        print("I am Shizuka. My hoby is singing", end ="\n\n")
        
        
        
shizuka = Shizuka() #shizuka object can access Doremon_class's method
shizuka.gadget()

shizuka = Shizuka() #shizuka object can access Doremon_class's method
shizuka.nobita_self()