#variable scope = where a variable is visible and accessible
#scope resolution = (LEGB) Local > Enclosed -> Global -> Built-in

def func1():
    a=4
    print(a)

# variable a and b are within the local scope ,within the scope of func1 
# and func2 respectively

def func2():
    b=9
    print(b)

func1()
func2()    

def func3():
    x=7
    def func4():
      x=8
      print(x)
    func4()
# a function encolsed under another function 
# if x used under func4 we using local version
# if x used under func3 we using enclosed version 
func3() 

# you can see below variable x is declared outside the two 
# function making it global  

def func5():
   print(x)

def func6():
      print(x)

x=7
func5()
func6()      

#below shows how e is built-in value     
from math import e

def func7():
    print(e)

func7()