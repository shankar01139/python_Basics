# #exception Handling in Python

# # 1.Division by zero Exception
# x=int(input("Enter an Integer :"))
# print(x/0)

# # 2.Syntax error handling
# synt=input("Enter Syntax to Display sum of values at variable a and b :")
# if ('+' in synt):
#     print("Syntax Correct...")
# else:
#     print("Enter Valid Syntax....")

# # 3.File not found Exception
# fname=input("Ënter File Name :")
# fp=open(fname,"r")

# # 4.Recursion
# def Repeat():
#     return Repeat()
# Repeat()

# # 5.User-defined Exception
# class NotEligibleException(Exception):
#     pass
# def AgeException(Age):
#     try:
#         if Age >= 18:
#             print("You are Eligible to Vote !")
#         else:
#             raise NotEligibleException
#     except NotEligibleException:
#         print('You are Not Eligible to Vote !')
# Age = int(input('Enter Your Age To Check Voter Eligibility :'))
# AgeException(Age)

# # 6.Multiple Exception
# def variousException():
#     my_list = [1, 2, 3, 4]
#     try:
#         a = 5
#         print(a)
#         print(my_list[5])
#     except (NameError, IndexError):
#         print('Error')
# variousException()

# # 7.Finally
try:
    fp=open("data.txt","r")
    fp.read(17)
except:
    print("File Not Found Exception.....!")
finally:
    fp.close()
