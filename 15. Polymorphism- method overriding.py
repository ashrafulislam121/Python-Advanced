class Human:
    def __init__(self, name):
        self.name = name
    
    def show_info(self):
        print(self.name)
        print("------Human class-------")
     
          
     
class Robot(Human):
    def __init__(self, name):
        self.name = name
    
    # def show_info(self):
    #     print(self.name)
    #     print("------Robot Class------")
        
        
human = Human("Nobita")
robot = Robot("Sophiya")

for i in (robot, human):
    i.show_info()