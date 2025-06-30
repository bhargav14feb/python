# there are two types of function in this tech world
# 1. Is inbuilt function (len(), upper, lower, startswith )
# 2. user defined function 
'''
def any variable():
    your code 

your variable 
'''
def functus():
    a= int(input("Enter a number:"))
    b= int(input("Enter a number:"))
    c= int(input("Enter a number:"))
                
    average= (a+b+c)/3
    print(average)

functus()

def good_morning (name):
    print(f"good morning {name}")

good_morning("bhargav")

def hello(name, ending="thank you"):  #function with arguement 
    print("hello" + name + ending) 

hello("bhargav","have a good day")
hello("ashwin")

def hello(name, ending=" thank you"):  #function with arguement 
    print("hello, " + name +  ending) 
    return "please print hello (your name,ending)"

hello("bhargav"," have a good day")
hello("ashwin")

a= hello("bhargav","have a good day")
print(a)


