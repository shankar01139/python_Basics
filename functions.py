# Python Functions

# 1.program to split vowels and consonents
def wordSplit(word):
    vowel_count = 0
    conso_count = 0
    for i in word:
        if i in 'aeiou' or i in 'AEIOU':
            vowel_count +=1
        else:
            conso_count +=1
    return 'The String include ' +str(vowel_count)+' Vowels and '+str(conso_count)+' Consonents .......'
print(wordSplit('shankaranarayanan'))

# 2.In BlackJack, cards are counted with -1, 0, 1 values:
# 2, 3, 4, 5, 6 are counted as +1
# 7, 8, 9 are counted as 0
# 10, J, Q, K, A are counted as -1
# Create a function that counts the number and returns it from the list of cards provided.
def count(deck):
    x=[2,3,4,5,6]
    y=[7,8,9]
    z=[10,'J','Q','K','A']
    tot=0
    for i in deck:
        if i in x:
            tot+=1
        elif i in y:
            tot+=0
        elif i in z:
            tot-=1
    return(tot)
print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
print(count(["A", "A", "K", "Q", "Q", "J"]))
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))

# 3.Rock-Paper-Scissors
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
def rps(p1,p2):
	v = {'Rock':1, 'Paper':2, 'Scissors':3}
	return ["It's a draw", 'The winner is p1', 'The winner is p2'][v[p1]-v[p2]]
print(rps("Rock", "Paper"))
print(rps("Scissors", "Paper"))
print(rps("Paper", "Paper")) 

# 4.Sorted or not?
def is_in_order(txt):
	return list(txt) == sorted(txt)
print(is_in_order("abc"))
print(is_in_order("edabit")) 
print(is_in_order("123"))
print(is_in_order("xyzz")) 

# 5.ATM PIN Code Validation
def is_valid_PIN(pin):
    if len(pin) in [4, 6] and pin.isdigit():
        return True
    return False
print(is_valid_PIN("1234"))
print(is_valid_PIN("14534"))
print(is_valid_PIN("45a2"))

# 6.default argument function
def student(firstname, lastname ='Mark', standard ='Fifth'): 
	print(firstname, lastname, 'studies in', standard, 'Standard') 

student('John') 			 
student('Bill', 'Gates', 'Seventh')	 
student('David', 'Gates')				 
student('Prem', 'Seventh') 

# 7. keyword arguments functions
def maths(a, b, c):
    x1 = a + b * c
    x2 = a + b / c
    return (x1 + x2), (x1 - x2) 
print(maths(a=31, b=93, c=62))
print(maths(c=62, b=93, a=31))

# 8.key-value pair argument function
def keyVal(**kwargs) :
    for key, value in kwargs.items() :
        return kwargs
print(keyVal(First_Name='Thiyash',Last_Name='Abimanyu', Gender='Male',roll=12, Dept='Software System')) 

# 9.Arbitrary Arguments function
def greet(*names):
    for name in names:
        print("Hello "+name +"! Hope You are Doing Good...")
greet("Ram", "Ravi", "Ragu", "John")

# # 10.recursion function
limit=int(input('Enter Limit :'))
def sum_recursive(current_number, accumulated_sum):
    if current_number == limit:
        return accumulated_sum
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)
print(sum_recursive(1, 0))