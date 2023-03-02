class Cartoon:
    "This is a Cartoon Class"
    series = "TV Series"
    
    #The self parameter is a reference to the current instance of the class, 
    #and is used to access variables that belongs to the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #All method in class contain self as a first parameters
    def show(self):
        print(self.name)
        print(self.age)
        print(self.series)
        
#Constructor in python is a special method that is called when an object is created. 
#The purpose of a python constructor is to assign values to the data members within the class when an object is initialized.
ob1 = Cartoon("Doreamonnnnnn",18)
ob2 = Cartoon("Shinchan",5)


#Modifier object properties
ob1.name = "Doreamon"

# print(ob1.name)
# print(ob1.age)
# print(ob1.series)
ob1.show()

# print(ob2.name)
# print(ob2.age)
# print(ob2.series)
ob2.show()

#Build-in method
print(Cartoon.__doc__)

print(ob1.__dict__)


