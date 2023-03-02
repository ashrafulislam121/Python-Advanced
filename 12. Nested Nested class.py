class Human:
    def __init__(self, name):
        self.name = name
    
    def show_info(self):
        print(self.name)
        print("------Human class-------")
     
        
     
        
     
    class Robot:
        def __init__(self, name):
            self.name = name
        
        def show_name(self):
            print(self.name)
            print("------Robot Class------")
            
            
        
        class Robo:
            def __init__(self, name):
                self.name = name
                
            def show_details(self):
                print(self.name)
                print("------Robo Class---------")



human = Human("Nobita")
human.show_info()

# #accessing nested_class, main_class help us.
# robot = human.Robot("Sophiya") #accessing Robot_class, Human_class help us 
# robot.show_name()

robo = human.Robot.Robo("Marquee")
robo.show_details()