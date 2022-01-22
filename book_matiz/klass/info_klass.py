# Два класса для мото и авто
# в Первом название разновидность и сколько лет в Эксплатации.  
# во Втором более подробная инфа

class One():
    def __init__(self,name,let,sity):
        self.name=name
        self.let=let
        self.sity=sity

    def name(self):
        if self.name=="moto":
            print(Two.mot())



class Two(One):
    def __init__(self, name, let, sity):
        super().__init__(name, let, sity)
    
    def moto(self):
        print(self.name )
1
    
x=One("moto",10,"msk")