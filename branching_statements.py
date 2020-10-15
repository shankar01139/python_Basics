# I.Simple If Statement

# 1.program to check if the number is divisible of 100 or not.
def divisible(num):
    if num % 100 == 0:
        return True
    return False
print(divisible(200))
print(divisible(202))

# 2.program to check if the string starts with vowel or not.
def vowels(string):
    if string[0] in 'AEIOU' or string[0] in 'aeiou':
        return True
    return False
print(vowels('activity'))
# print(vowels('python'))

# II.Nested if...else Statement

# 3.program to check if the number is greater than 50 and divisible by 2.
def checkNum(num):
    if num>50:
        if num % 2 ==0:
            return 'The given number '+str(num)+' is Greater than 50 and divisible by 2'
        else:
            return 'The given number '+str(num)+' is Greater than 50 but not divisible by 2'
    else:
            return 'The given number '+str(num)+' is Less than 50'
print(checkNum(60))
print(checkNum(55))
print(checkNum(23))

# 4.Driving License Eligibility
def driving(age,aadhar):
    if age>=18:
        if aadhar == True:
            return 'You are Eligible to apply for Driving License'
        else:
            return 'You are Eligible to apply for Driving License Only if you have Aadhar Card'
    else:
            return 'You are Not Eligible to apply for Driving License'
print(driving(23,True))
print(driving(19,False))
print(driving(16,True))


# III.If....Elif Statement
5. program to use if...elif statement in list
lst=[10,11,12,13,14]
if lst[0] == 10:
    print('First Element of list is 10')
elif lst[1] == 11:
    print('Second Element of list is 11')
else:
    print('First and Second Element of list is not 10 and 11')

# 6.program to use if...elif statement 
num=int(input("Enter An number :"))
if num %3 == 0 and num %2 != 0 :
    print('Number is Divisible by 3')
elif num %2 == 0 and num %3 != 0:
    print('Number is Divisible by 2')
elif num %2 == 0 and num %3 == 0:
    print('Number is Divisible by both 2 and 3')
else:
    print('Number is not Divisible by both 2 and 3')

# IV.break Statement
# # 7.program to work with python break statement
season='winters'
word=''
for i in season:
    if i == 's':
        break
    word +=i
print(word)

# 8.program to work with python break statement
for i in range(1,10):
    if i *i == 25:
        break
print("Number Reached Five")

# V.Continue Statement
# 9.program to work with python continue statement
for number in range(1,50):
    if number %2 == 0:
        continue
    print(number)

# 10.program to work with python continue statement
 for number in range(1,100):
    if number %5 == 0:
        continue
    print(number)