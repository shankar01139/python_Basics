#Classes and Objects in python
# 1.General Classes
# class Stud:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def myfunc(data):
#     print("Hello " + data.name+"...!")
# p1 =Stud("Shankar", 23)
# p1.myfunc()

# class mark:
#   def __init__(self, m1, m2,m3):
#     self.m1 = m1
#     self.m2 = m2
#     self.m3 = m3
#     sum=self.m1+self.m2+self.m3
#     print("Total mark : ",sum)
# p1 =mark(90,83,77)

# 2.Object as Argument
# class Stud:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#     def display(self):
#         print("Name-", self.name)
#         print("Grade-", self.grade)
# obj = Stud("Shankar",'A')
# obj.display()

# class Emp:
#     def __init__(self, ename, salary):
#         self.ename = ename
#         self.salary = salary
#     def display(self):
#         print("Name-", self.ename)
#         print("Salary-", self.salary)
# obj = Emp("Ram", "21560")
# obj.display()

# 3.Method Overidding
# class Rectangle():
# 	def __init__(self,l,b):
# 		self.l = l
# 		self.b = b
# 	def getArea(self):
# 		print("Area of Rectangle : ",self.l*self.b)
# class Square(Rectangle):
# 	def __init__(self,side):
# 		self.side = side
# 	def getArea(self):
# 		print("Area of Square : ",self.side*self.side)
# s = Square(4)
# r = Rectangle(2,4)
# s.getArea()
# r.getArea()

# class Employee:
#     def message(self):
#         print('This message is from Employee Class')
# class Department(Employee):
#     def message(self):
#         print('This message is from Department class')
# emp = Employee()
# dept = Department()
# emp.message()
# dept.message()
 
# 4.Encapsulation
# class Stud:
#   def Stud1(self):
#     return 'you can write the test...'
#   def __Stud2(self):
#     return 'you cannot Write the test..'
# Check = Stud()
# print(Check.Stud1())
# print(Check._Stud__Stud2())

# class Emp:
#   def Emp1(self):
#     return 'Aurthorization Successfull...'
#   def __Emp2(self):
#     return 'Unaurthorized Access...'
# Check = Emp()
# print(Check.Emp1())
# print(Check._Emp__Emp2())

# 5.Inheritance
# class Person:
#   def __init__(self, fname, id ,position):
#     self.firstname = fname
#     self.id = id
#     self.position = position
#   def Details(self):
#     print(self.firstname, self.id, self.position)
# class Emp(Person):
#   pass
# x = Person("Shankr", "12101","Developer")
# x1 = Emp("Ragu", "12103","Manager")
# x.Details()
# x1.Details()

# class Robot:
#     def __init__(self, name):
#         self.name = name     
#     def greet(self):
#         print("Hi, I am " + self.name)       
# class PhysicianRobot(Robot):
#     pass
# x = Robot("Prem")
# y = PhysicianRobot("Rajesh")
# x.greet()
# y.greet()
 