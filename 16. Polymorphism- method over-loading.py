class Profile:
    def name(self, first=None, middle = None, last=None):
        if first !=None and middle != None and last != None:
            print(first+ middle + last)
        elif first !=None and middle != None:
            print(first+ middle)
        else: 
            print(first+ middle)
            
            

p = Profile()
p.name("Ashraful","Islam")