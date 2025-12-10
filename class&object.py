#class 
class abc():
    var=100
    def display(self):
        print("This is a cls method")
obj=abc()
print(obj.var) #or print(abc.var)
obj.display() 
