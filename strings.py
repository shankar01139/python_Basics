# Strings in python
# 1.len function
str='shankaranarayanan'
ary=[10,20,30,40,50,60,70,87,90]
tup=(23,45,56,78,'ragu','rajesh',True)
lst=['Paurnami','shankar',23,False]
dct={'Tamil': 89,'English':100,'Maths':92,'Science':75}
print("Python len() Function ....")
print(".....")
print("Length function in String : ",len(str))
print("Length function in Array : ",len(ary))
print("Length function in Tuple : ",len(tup))
print("Length function in List : ",len(lst))
print("Length function in Dictionary : ",len(dct))

# # 2.Simple String 
count=int(input("Enter Count : "))
i=1
while(i<=count):
    str=input("Enter String %s : "%i)
    i+=1
   
# 3.Concatenation of Strings
str1='Shankar '
str2='Krishna'
print("String Concatenation using + Operator :",str1+str2)
print('String Concatenation using join() Function :'.join([str1,str2]))
print('String Concatenation using format() Method :{}{}'.format(str1,str2))

# 4.String Slicing
strng=['P', 'y', 't', 'h', 'o', 'n']
print("Slicing String with index :",strng[3:5])
print("Slicing String with  Negetive index :",strng[1:-3])
print("Slicing String with Hopping with index :",strng[2:15:2])
slice_object = slice(1, 4, 1) 
print("Slicing String with slice() Method :",strng[slice_object])
slice_object = slice(-1, -5, -2)
print("Slicing String with Negative Indexed slice() Method :",strng[slice_object])

# 5.Repitation of Strings
str='shankaranarayanan'
print("Using * :",str*3)
print("Using * :",str[3:6]*3)
        
# 6.String Traversal
strng= "shankaranarayanan"
letter=input("Choose Letter :")
count=0
for char in strng:
   if char == letter:
       count+=1
print("The String includes {} no.of {}".format(count,letter))

# 7.Escape chartacters Program
txt = "Im shankaranarayanan ,\"27 years old\""
txt1 = "Im shankaranarayanan ,\n27 years old"
txt2 = "Im shankaranarayanan ,\t27 years old"
txt3 = "Im shankaranarayanan ,\r27 years old"
txt4 = "Im shankaranarayanan ,\f27 years old"
txt5 = "Im shankaranarayanan ,\b27 years old"
print(txt)
print(txt1)
print(txt2)
print(txt3)
print(txt4)
print(txt5)

# 8.String Formating Functions
str1='shankar'
str2='Krishna'
print('String formating using format() Method :{}{}'.format(str1,str2))

a=23
b=44
c=a+b
print('Sum of {0} and {1} : {2}'.format(a,b,c))

a='shankar'
print('Your Name is %s'%a)




















