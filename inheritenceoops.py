class weakhero:
    def __init__(self,name):
        self.name=name
        self.is_fighting=True

    def fight(self):
        print(f'{self.name} likes to fight')

        
    def eat(self):
        print(f'{self.name} likes to eat')


class ml(weakhero):
    pass

class ml2(weakhero):
    pass

class nrl(weakhero):
    pass


mL=ml("yeon sieun")
mL2=ml2("ahn-suho") 
nRl=nrl("oh beomseok")      

print(mL.name)
print(mL2.name)
print(nRl.name)
print(mL2.is_fighting)
mL2.eat()
mL.fight()