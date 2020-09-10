#CREATE CLASS
class bank():
    def __init__(self,ownername,balance):
        self.ownername=ownername
        self.balance=balance
    def deposit(self,det_amt):
        self.balance += det_amt
        return ("deposited")
    def withdraw(self,withdraw):
        if self.balance >= withdraw:
            self.balance -= withdraw
            
            return ("withdraw accepted")
        else:
            print("not upto ur balance")
    
k=bank("karishma",5000)
print(k.deposit(100))
print(k.withdraw(400))




#CONE
import math
class cone():
    def __init__(self,r,h):
        self.r=r
        self.h=h
    def volume(self):
        b=3.14*self.r*self.r*(self.h/3)
        return (b)
    def surfacearea(self):
        c=3.14*self.r*self.r
        return (c)
    def side (self):
        d=3.14*self.r*math.sqrt(self.r*self.r+self.h*self.h)
        return (d)
p=cone(1,2)
print(p.volume())
print(p.surfacearea())
print(p.side())
    
    
