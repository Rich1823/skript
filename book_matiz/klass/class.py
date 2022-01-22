
class Info():
    def __init__(self,x,y):
        self.nam1 = x
        self.nam2 = y
        self.z = 100
        
    
    def pr(self):
        if self.nam1==0:
            return("No")
        else:
            return(self.nam1+self.nam2+self.z**2) 

x =int(input())
y=int(input())
my=Info(x,y)
print(my.pr())