# Python Dictionary
# 1.General Dictionary - 2 
# Merge dict using update() method
# def Merge(dict1, dict2):
# 	return(dict2.update(dict1))
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# Merge(dict1, dict2)
# print(dict2)
# print('------------------------')
# Remove double quotes from dictionary keys 
# dict = {'"Shankar"' : 3, '"Ram"' : 5, '"R"agu' : 9} 
# print("The original dictionary is : " + str(dict)) 
# res = {key.replace('"', ''):val for key, val in dict.items()} 
# print("The dictionary after removal of double quotes : " + str(res)) 

# print('------------------------')
# 2. Program using dict keyword
# lst=[['a',23],['b',27],['c',91]]
# dict1 = dict(zip(['Shankar', True, 'Prem'], [1, 2, 3]))
# dict2 = dict(lst)
# print(dict1)
# print(dict2)
# print('------------------------')
# 3. Accessing Dictionary Elements
# dict1={'Name' : 'shankar' , 'Age' : 23 ,'HasVoter_ID' : True }
# if dict1['Age'] > 18 and dict1['HasVoter_ID'] == True:
#     print('You are Eligible to vote!')
# else:
#     print('You are Not Eligible to vote!')
# print('------------------------')
# 4. Updating Dictionary
# dict1={'Name' : 'shankar' , 'Age' : 23 ,'HasVoter_ID' : True }
# dict2={'Gender' : 'Male'}
# dict1.update(dict2)
# print('By adding element from Another Dictionary :',dict1)
# dict1.update(Status = 'Single')
# print('By adding element from Another Tuple :',dict1)
# dict1['Age']=27
# dict1['HasVoter_ID']=False
# print('By Changing Existing Elements in Dictionary :',dict1)
# print('------------------------')
# 5. deleting Dictionary (del,pop,clear)
# dict1={'Name': 'shankar', 'Age': 27, 'HasVoter_ID': False, 'Gender': 'Male', 'Status': 'Single'}
# dict1.pop('Gender')
# print("Dictionary After pop() :",dict1)
# dict1.popitem()
# print("Dictionary After popitem() :",dict1)
# dict1.clear()
# print("Dictionary After clear() :",dict1)
# del dict1
# print("Dictionary After del keyword :",dict1)
# print('------------------------')
# 6. Traversing a Dictionary
# NamesAndAge = {'Shankar': 23 , 'Vinith' : 27, 'Sarath':17  , 'Ragu' : 33  } 
# print('Traverse Through Keys : ')
# for Name in NamesAndAge: 
#     print('Hello..'+Name+' Hope You are Doing Good.....')
# print('---------')
# print('Traverse Through Values : ')   
# for Age in NamesAndAge:
#     if(NamesAndAge[Age] > 18):
#         print('You can Apply for Licence...')               
#     else:
#         print('You have to couple of years to Apply for Licence... ')
# print('---------')
# print('Traverse Through Key and Value Pair : ')   
# for Name , Age in NamesAndAge.items():
#     print(Name + '.You are '+str(Age)+' Years Old...')
# print('------------------------')
# 7. Membership Operator in Dictionary
# dict1={'Shankar': 23 , 'Vinith' : 27, 'Sarath':17  , 'Ragu' : 33  } 
# keyval=input('Enter Your Name : ')
# if keyval in dict1:
#     print('Your Name is Present in the Dictionary..')
# else:
#     print('Your Name is  not Present in the Dictionary..')
# print('------------------------')
# 8. Dictionary length 
# dict1={'Name' : 'shankar' , 'Age' : 23 ,'HasVoter_ID' : True }
# dict2={'Gender' : 'Male'}
# print('Length of the Dictionary Before Adding New Element : ',len(dict1))
# dict1.update(dict2)
# print('Length of the Dictionary After Adding New Element : ',len(dict1))
# # print('------------------------')
# 9 Sorting a Dictionary
from collections import OrderedDict 
dict1 = {'ravi':10,'Shankar': 23 , 'Vinith' : 27, 'rajnish':9,'sanjeev':15,'Sarath':17 ,'yash':2,'suraj':32} 
dict2 = OrderedDict(sorted(dict1.items())) 
print(dict2) 