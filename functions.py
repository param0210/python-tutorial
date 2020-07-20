#python functions and their types

#function vs method
#A method refers to a function which is part of a class.
# You access it with an instance or object of the class. 
# A function doesn’t have this restriction: 
# This means that all methods are functions, but not all functions are methods.

# Define a function `plus()`
def plus(a,b):
  return a + b

#calling the function into another function
def minus(n1,n2):
    plus_value=plus(n1,n2) #here calling the plus function and using its value to calculate the minus value
    minus_value=30-plus_value
    return minus_value

var1,var2=5,5
minus_=minus(var1,var2)
print(minus_)


#Create a `Summation` class
class Summation(object):
  def sum(self, a, b):
    self.contents = a + b
    return self.contents 

 #calling a method of a class
    
summ=Summation()  #first create an object of a class
summ.sum(5,5) #then access method with that object


#types of function arguments
#1.default arguments
#2.required arguments
#3.keyword arguments
#4.valiable numbers of arguments


#1.default arguments

def sum_(a=10,b=7):
  return a+b


print("sum of numbers:",sum_())

#when the no arguments are passed during function call it will take default arguments 
#another example

def substraction(var1=10,var2=5):
  return var1-var2

result=substraction(var1=20)
print("result is:",result)

#2.required arguments
#the required numbers of arguments should be passed during function call


#3.keyword arguments
#used to make sure that you are passing the arguments in the right order

def division(a,b):
  return a//b

print("division of numbers is:",division(a=10,b=2))


#4.variable numbers of arguments
#when you dont know the numbers of arguments passing to the function
def args(*args):
    print("args are:",args)
    return sum(args)

print("sum of all numbers",args(1,4,5))


# local vs gloabl varialbe
# a variable that is defined inside a function body is called local varible and variable that is outside function body 
#is called global variable and can accessed globally

variable=10
def all(*args):
  print("args:",args)
  for i in args:
    pass
  

print("all numbers are:",all(1,2,3,4,5,6,7,8,9))



