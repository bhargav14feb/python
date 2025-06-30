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
# n= int(input("Enter a number:"))

# for i in range (1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

# virtual bank

# balance = int(input("Enter your bank balance: "))

# while True:
#     print("\nChoose")
#     print("1. Your bank balance")
#     print("2. Cash deposit")
#     print("3. Cash withdrawal")
#     print("4. Exit")

#     a = input("Enter your option: ")

#     if a == "1":
#         print(f"Your balance is ₹{balance}")

#     elif a == "2":
#         amount = float(input("Enter the amount you want to deposit: "))
#         balance += amount
#         print(f"Deposited ₹{amount}. New balance is ₹{balance}")

#     elif a == "3":
#         amount = float(input("Enter the amount you want to withdraw: "))
#         if amount > balance:
#             print("Insufficient balance!")
#         else:
#             balance -= amount
#             print(f"Withdrawn ₹{amount}. New balance is ₹{balance}")

#     elif a == "4":
#         print("Thanks for banking with us 🙏")
#         break

#     else:
#         print("Invalid option. Please enter 1 to 4.")


