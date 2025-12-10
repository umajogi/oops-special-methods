#class constructor __init__ method
class abc():
    def __init__(self,value):
        print("this is a cls method")
        self.value=value
        print("the value is:",value )
obj=abc(10)
