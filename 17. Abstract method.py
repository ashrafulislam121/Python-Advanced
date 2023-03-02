""" 
An abstract class is used if you want to provide a common, implemented functionality among all the implementations of the component. 
"""

from abc import ABC, abstractmethod #ABC = Abstract base Class

class Father(ABC): #abstact class
    @abstractmethod
    def go_school(self):
        pass  #abstractmethod always will be empty
        
        
    #concrete method
    def result(self):
        print("Haa , result diche...")
        
class Nobita(Father):
    def go_school(self): #must be remain cause it's abstract method mensioned before
        super().result()
        print("Haa, School a gechi")
        
    def playing(self):
        print("playing Football")
        
    def singing(self):
        print("Singing")
        

nobita = Nobita()
nobita.playing()
