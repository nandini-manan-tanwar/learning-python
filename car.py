class car:
    def __init__(self,brand,speed,year,owner):
        self.brand=brand
        self.speed=speed
        self.year=year
        self.owner=owner

    def accelerate(self):
        self.speed +=10