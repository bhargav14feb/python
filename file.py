# st= "hello guys i am writing in a file, this is complete magic, you can do anything you want, this is the best game"
# f= open("text.txt","w")
# data=f.write(st)
# print(data)
# print(type(data))
# f.close() 

# f= open("text.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close() 

# st= "hello guys i am writing in a file, this is complete magic, you can do anything you want, this is the best game"
# f= open("text.txt","a")
# data=f.write(st)
# print(data)
# print(type(data))
# f.close() 

# f= open("text.txt")
# line= f.readlines()
# print(line)


# f= open("text.txt")

# line1= f.readline()
# print(line1)
# print(type(line1))

# line2= f.readline()
# print(line2)
# print(type(line2))

# line3= f.readline()
# print(line3)

# line4= f.readline()
# print(line4)

# line5= f.readline()
# print(line5)

# f= open("text.txt")
# data= f.readlines()
# print(data)

# with open("text.txt") as f:
#     data= f.read()
#     if "this" in data:
#         print("yes this contains 'this'")
     



# with open("text.txt") as f:
#     data= f.readlines()
#     n=0
#     while n<len(data):
#         print(data[n])
#         n+=1
        
    
# print(data[0])
# print(data[1])

import random
your_score=random.randint(1,69)
highscore=0
with open("text.txt","w") as f:
    if your_score>highscore:
        data=f.write(str(your_score))
    else:
        data=f.write(str(highscore))
