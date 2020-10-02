'''
this tutorial will define about class variables and instance variables
'''


class Student:
    semesters=2 #class variable
    pass

#here we are creating 2 objects from class student 
std1=Student()
std2=Student()

#here name is intsnace varible
#'name' is instance's own property it is not inherited from class 
std1.name="xyz"

# accessing class variables with object
print(std1.semesters)
print(std1.semesters)

#accessing class variable with class name
print(Student.semesters)

#changing the class variable value
#we can change it only with class name 
#instances can't change class variable value
Student.semesters=3
print(Student.semesters)