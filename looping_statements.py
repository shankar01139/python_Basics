# I.for loop

# 1.program to print first 20 natural number
for i in range(1,20):
    print(i)
    i+=1

# 2.program to print square of numbers
num=int(input('Enter Limit :'))
for i in range(1,num):
    print(i ** 2)
    i+=1

# 3.program to get three numbers (a,b,c) and check how many numbers between 'a' and 'b' are divisible by 'c'
a=int(input("Enter Number 1 :"))
b=int(input("Enter Number 2 :"))
c=int(input("Enter Number 3 :"))
for i in range(a,b):
    if(i % c ==0):
        print(i)

# 4.program to remove vowels in a word
word=input('Enter a word : ')
vowels=('a','e','i','o','u')
for letter in word.lower():
    if letter in vowels:
        word=word.replace(letter,"-")
print(word)

# 5.program to print all the numbers divisible by 5 from list
lst=[11,20,6,15,7,25,30,41]
for i in lst:
    if i % 5 ==0:
        print(i)


# II.while Statement

# 6.program to print sum of Digits
num=int(input('Enter a Number : '))
sum=0
rem=0
while num !=0:
    rem =num % 10
    sum +=rem
    num //=10
print('Sum of Digits :',sum)

# 7.program to print first 20 natural number
i=0
while i<=20:
    print(i)
    i+=1

# 8.program to print right angle triangle
i=1
limit=int(input('Enter Limit  :'))
while i<=limit:
    print('*' *i)
    i+=1

# 9.program to print numbers divisible by user given value
diviser=int(input('Enter Diviser Value :'))
i=1
while i in range(1,100):
    if i % diviser ==0:
        print(i)
    i+=1

# 10.Hopping Numbers
i=1
limit=int(input('Enter Limit  :'))
while i<=limit:
    print(i)
    i+=1

