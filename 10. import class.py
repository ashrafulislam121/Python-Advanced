#import a class

# from first_module import Robot as r
# from first_module import Human as h
import first_module as f #import entire module
from second_module import Animal as a #import single_class from module_into_module

print("---------------Robot-------------")
robot = f.Robot("Sophiya", "6 years")

robot.show_name()
robot.show_age()


print("---------------Human-------------")
human = f.Human("Shinchan", "5 years", "Apple")

human.show_name()
human.show_age()
human.show_food()

print("---------------Animal-------------")
animal = a("Shiro", "3 years", "Cake","Pet Animal")

animal.show_name()
animal.show_age()
animal.show_food()
animal.show_pet()
