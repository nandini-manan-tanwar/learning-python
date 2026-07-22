class animal:
    alive=True

class dog(animal):
    def speak(self):
        print("woof woof")


class cat(animal):
    def speak(self):
        print("meow meow")
        
class duck(animal):
    def speak(self):
        print("quack quack")

class car(animal):
  def speak(self):
      print("honk honk")
animals=[dog(),cat(),duck(),car()]

for y in animals:
    y.speak()