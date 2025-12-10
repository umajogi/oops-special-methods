class abc():
    cv=0
    def __init__(self,val):
        abc.cv+=1
        self.val=val
        print("class variable",abc.cv)
        print("object variable",val)
    def __del__(self):
        print("object with %d is going out of scope" %self.val)

obj1=abc(10)
obj2=abc(20)
del obj1
del obj2
