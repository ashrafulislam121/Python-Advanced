# a = 5 
# b = 5

# print(a+b)  #when + sign come, it call __add__() method
# print(a.__add__(b))

class Number:
    def __init__(self, no):
        self.no = no
    
    def __add__(self, num):
        return str(self.no) + str(num.no)+"fun"
    
    def show(self):
        print(self.no)

    
a = Number(35)
b = Number(5)

print(a.__add__(b))
print(a+b)
