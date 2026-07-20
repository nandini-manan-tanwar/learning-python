class student:
   number_student=0
   grad_year= 2026
   def __init__(self,name,grade,id_number):
        self.name=name
        self.grade=grade
        self.id_number=id_number
        student.number_student +=1
student1=student("nandini","D","iz457")
student2=student("harshi","k","iz458")   
student3=student("suhani","l","iz459")        
print(f"grad year: {student1.grad_year}")
print(f"{student1.name}'s id number is :{student1.id_number}")
print(f"number of student = {student.number_student}")
print(f"class of {student.grad_year} has {student.number_student} students")