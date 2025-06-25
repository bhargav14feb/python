# loops can be used to reapeat a set of work
# there are two types of loops, both can be used to perform a single set of work
''''
while (condition):
    task 
    something which can close the condition
'''
# a = 0

# while a <6:
#     print(a)
#     a += 1


# # same task can be done in for loop
# for list in range (1,11):
#     print(list)

# some projects under for loops 

# table of n
# n= int(input("Enter a number:"))

# for i in range (1,11):
#     print(n,"*",i,"=", n*i)

# star pattern

'''
n=3
   *
  ***
 *****
'''
n= int(input("Enter a number:"))

for i in range (1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")
