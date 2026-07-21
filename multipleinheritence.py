class animal():
    def __init__(self,name):
        self.name=name
    def sleeping(self):
        print(f"{self.name} is eating")

class prey(animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class predator(animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class tiger(predator):
    pass

class deer(prey):
    pass


class fish(predator,prey):
    pass

Tiger=tiger("tiger")
Deer=deer("deer")
Fish=fish("fish")
Tiger.hunt()
Fish.flee()
Tiger.sleeping()
