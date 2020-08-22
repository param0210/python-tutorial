#difference between print() and return statement
#return is used to return value from function that may be used further but if we want to print that particular value on 
#console we use print() statement

def sum(a,b):
    return a+b

def substraction(n1,n2):
    plus=sum(n1,n2)
    return plus-10

output=substraction(10,20)
print("output is",output)