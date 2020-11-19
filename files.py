#Files in python
# 1.Reading a file
# fp=open("input.txt","r")
# print(fp.read())
# print(fp.read(7))

# 2.Writing into a file
# (!)with write mode
# fp=open("input_copy.txt","w")
# fp.write("Written with write mode....")
# fp=open("input1.txt","w")
# fp.write("Written with write mode....")

# (!)with append mode
# fp=open("input_copy.txt","a")
# fp.write(" Written with append mode....")
# fp=open("input2.txt","a")
# fp.write("Written with append mode....")

# 3.tell() method
# fp=open("input.txt","r")
# print("Position before Reading or Writing : ",fp.tell())
# fp.read(5)
# print("Position after Reading or Writing : ",fp.tell())

# # 4.seek() method
# fp=open("input.txt","r")
# pos=int(input("Which Position You want to move the Cursor  : "))
# print("Position of Cursor : ",fp.seek(pos))
# print("File Content From "+str(pos)+"th location : ",fp.readline())

# 5.Deleting a file
# import os
# os.remove("data.txt")
# print("File Successfully Deleted")

# 6.Renaming a file
# import os
# os.rename("renaming.txt","renamed.txt")
# print("File Successfully Renamed")

#7.File Creation
# fp=open("Creation.txt","x")
# print("File Successfully Created")




