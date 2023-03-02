"""
Encapsulation refers to the bundling of data, along with the methods that operate on that data, into a single unit.
"""
class Nobita:
    def __init__(self):
        self.book = "Comics"
        self.no = 10 #public
        self._no= 20 #protected
        self.__no = 30 #private
        
    def show(self):
        print(self.no, self._no, self.__no)
        
class Sonio(Nobita):
    def show_nobita(self):
        print("Sonio: ", self._no)
        print("Sonio: ", self._Nobita__no) #to show private data , need to know it's class name


nobita = Nobita()
sonio = Sonio()

nobita.show()
sonio.show_nobita()