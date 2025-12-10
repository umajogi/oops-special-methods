#cls object variables
class abc():
    cv=0
    def __init__(self,val):
        abc.cv+=1
        self.val=val
        print("object var:",val)
        print("class var:",abc.cv)
x=abc(10)
x=abc(20)
