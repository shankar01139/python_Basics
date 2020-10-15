# python tuples
# 1.General tuple
tup = (100 ,111, 112, 113,114,115) 
print(tup[1:]) 
print(tup[::-1]) 
print(tup[2:4]) 

tup=(False,20,30,True,50,20,60,'shankar',20 ,'ram')
print('Counting tuple elements with count() method : ',tup.count(20))  
print('Identifying the index of an particular element with index() method : ',tup.index('shankar'))

# 2.Tuples immutable with exception handling 
tup=(100,200,300,400,500)
print('Tuple before we try mutate the element:',tup)
print('')
print('If we try to mutate , It will show.....')
try:
  tup[3]='shankar'
except:
  print("TypeError: 'tuple' object does not support item assignment....")
  print('Because Python tuples are immutable...!')


# 3.Tuple conactenation
tup=(11, 'shankar', 13, True, 15, 16, 'Rajesh', 18)
tup1=(False,20,30,True,50,60)
print('Concatenation with + Operator :',(tup+tup1))
print('Concatenation with sum method :',sum((tup,tup1), ()))


# 4.Tuple Repitation
tup=(11, 'shankar', 13, True, 15, 16, 'Rajesh', 18)
print(tup)
rep=int(input('How many times do you want to repete the tuple:'))
print('Tuple Repitation:',tup*rep)


# 5.Tuple Length
tup1=(False,20,30,True,50,60)
lgth=int(input('Can you guess the legth of the list:'))
if(len(tup1) == lgth):
    print('WoW! You Guessed it correctly..!')
else:
    print('Nah! Try Again ..!')


# 6.Tuple Memebership
tup=(11,22,33,44,55,66,77,88,99)
var=int(input('Enter Data:'))
if var in tup:
    print('Data you entered is available in the tuple....') 
if var not in tup:
    print('Data you entered is Not available in the tuple....')


# 7.Tuple For loop
tup=(11, 'shankar', 13, True, 15, 16, 'Rajesh', 18)
for i in range(len(tup)):
    if isinstance(tup[i],bool):
        print("It is a Logical value ..")
    elif isinstance(tup[i],int):
        print('It is a Integer Value...')
    elif isinstance(tup[i],str):
        print('It is a String Value...')

    
# 8.Tuple Zip Function
tup1=('shankar',43,True,'ram',False)
tup2=('Vinith',43,False,'ragu',True)
for x, y in zip(tup1,tup2):
    if x == y:
        print(True)
    else:
        print(False)
zip_tuple=zip(tup1,tup2)
print(list(zip_tuple))


# 9.Tuple min max  
tup=((45,68),(27,89),(567,54),(98,117))
s1=sum(tup[0])
s2=sum(tup[1])
s3=sum(tup[2])
s4=sum(tup[3])
tup1=(s1,s2,s3,s4)
print('Minimum Value:',min(tup1))
print('Maximum Value:',max(tup1))


# 10.List into Tuple
lst=[11,'shankar',13,True,15,16,'Rajesh',18]
print('Data As List:',lst)
print('Converting List into Tuple.....')
print('Data As Tuple:',tuple(lst))