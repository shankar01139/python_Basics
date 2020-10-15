# # Python List
# # 1.General List
strng = input("Enter a list Elements :")
print(" ")
lst = strng.split()
print("The Given list is ",lst)
sum1 = 0
diff=0
mul=1
div=1
for num in lst:
    sum1 += int(num)
    diff -= int(num)
    mul *= int(num)
    div /= int(num)
print("Addition = ", sum1)
print("Subtraction = ", diff)
print("Multiplication = ", mul)
print("Division = ", div)


# # 2.List Copy
lst = ['shankar', 70, 6.7,True]
lst1 = lst[:]
lst2 = lst.copy()
print('Old List:', lst)
print('New List with copy() method :', lst1)
print('New List with slicing method :', lst2)


# # 3.Slicing
lst = ['Prem', 'yash', 'tarun', 'hari', 'shyam', 'naren']
print("List Slicing :",lst[slice(3)])
print("Slicing with Starting and Ending Index :",lst[slice(1,3)])
print("Slicing With Hopping :",lst[slice(1,5,1)])


# # 4.Deleting a List
lst1=[11,12,13,14,15,16,17,18]
lst2=[False,20,30,True,50,60]
lst3=[56,'prakash',34,64,'prem',87,9875,'ram']
lst4=[11,'shankar',13,True,15,16,'Rajesh',18]
print("List 1 Before Deleting :",lst1)
print("List 2 Before Deleting :",lst2)
print("List 3 Before Deleting :",lst3)
print("List 4 Before Deleting :",lst4)
lst1.clear()
lst2=[]
lst3*=0
del lst4[:]
print("List 1  After Deleting :",lst1)
print("List 2  After Deleting :",lst2)
print("List 3  After Deleting :",lst3)
print("List 4  After Deleting :",lst4)

# # 5.Traversal of List
lst=[11,'shankar',13,True,15,16,'Rajesh',18]
for i in range(len(lst)):
    print(lst[i])

# # 6.List Repitation , Concatenation and Length
lst2=[False,20,30,True,50,60]
lst3=['prakash',34,64,'prem',87,9875,'ram']
print("List Repitation :",lst2*3)
print("List Concatenation :",lst2+lst3)
print("Length of the List",len(lst3))

# # 7.Membership Operator
lst1=[11,12,13,14,15,16,17,18]
data=int(input("Enter Data :"))
if data in lst1:
    print("Data Available in the List..")   
elif data not in lst1:
    print("Data  Not Available in the List..")

# # 8.For Loop
lst = [1,2,3,4,5,6,7,8,9,10]
print(lst)
ele=int(input("Select an element from the list to Find the Location..:"))
for i in range(len(lst)):
    if ele == lst[i]:
        print("Number Found at the Location :",i)
               
# #9.List append
lst=['shankar','sathish','hari','pranesh']   
lst1=[23,False,65,True] 
print("List Before append() :",lst)
for i in range(len(lst1)):
    lst.append(lst1[i])       
print("List After append() :",lst)

# # 10.Insert and Extend
lst1=[23,False,65,True,'ram','ragu',47] 
lst2=[11,22,33,44]
lst3=[100,200,300,400,500]
print("List Before insert() and extend() :",lst1)
lst1.insert(5,'Prakash')
print("List After insert() :",lst1)
lst1.extend(lst3)
print("List After extend() :",lst1)
for i in range(len(lst2)):
    lst1.insert(5,lst2[i])
print("List After insert() :",lst1)
 