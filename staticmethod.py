class employee():
    def __init__(self,name,position):
        self.name=name
        self.position=position

    def info(self):
        print(f"{self.name} works as {self.position}")

    
    def is_position(position):
        positions=['WAITRESS','MANAGER','COOK','ACCOUNTANT']
        return position in positions

employee1=employee("riya","waitress")
employee2=employee("nandini","ACCOUNTANT")
employee2.info()
employee1.info()
print(employee.is_position("COOK"))
                