class Human:
    def __init__(self, name):
        self.name = name
    
    def show_info(self):
        print(self.name)
        print("------Human class-------")
     
          
     
class Robot:
    def __init__(self, name):
        self.name = name
    
    def show_info(self):
        print(self.name)
        print("------Robot Class------")
        
        
human = Human("Nobita")
robot = Robot("Sophiya")

for i in (human, robot):
    i.show_info()