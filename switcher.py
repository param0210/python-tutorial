#implementation of switch case in python
#switch cases are not available in python
#but this can be done using dictionary mapping

#we can also call a function as dictionary values
#for e.g.

def xyz():
    return "hello world"


#define a function

def switcher(value):
    dict={
        0:xyz(),
        1:"one",
        2:"two",
        3:"three",
    }
    return dict.get(value,"no option availabe for this")

user_input=int(input("enter the value"))
func_call=switcher(user_input)
print(func_call)

