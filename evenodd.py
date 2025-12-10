class number():
    e=[]
    o=[]
    def __init__(self,val):
        if val%2==0:
            self.e.append(val)
        else:
            self.o.append(val) 
n1=number(21)
n2=number(32)
n3=number(43)
n4=number(54)
n5=number(65)
print(number.e)
print(number.o)
