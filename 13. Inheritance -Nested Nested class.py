#Nested class is isolated from main class
# if we inharitence main class, we can't access methon within sub_class
class Human:
    def __init__(self, name):
        self.name = name
    
    def show_information(self):
        print(self.name)
        print("------Human class-------")
     
    class Robot:
        def __init__(self, name):
            self.name = name
        
        def show_details(self):
            print(self.name)
            print("------Robot Class------")
            
            
class Huma:
    def __init__(self, name):
        self.name = name
    
    def show_info(self):
        print(self.name)
        print("------Huma class-------") 
        
    class Robo(Human.Robot):
        def __init__(self, name):
            self.name = name
                
        def show_deta(self):
            print(self.name)
            print("------Robo Class---------")



robo = Huma.Robo("Marquee")
robo.show_details()
