##### ============== Class and Objects ================= #####

# Notes:
# A function that lives inside a class is called a method.
# So, methods are functions, but not all functions are methods.


# class Student:
#     def __init__(self):
#         self.name = "Sunil"
#         self.grades = (10,20,30)

#     def avg(self):
#         return sum(self.grades)/len(self.grades)


# student = Student()
# print(student.avg())


# class Student:
#     def __init__(self,name,grades):
#         self.name = name
#         self.grades = grades

#     def avg(self):
#         return sum(self.grades)/len(self.grades)


# student = Student("Sunil",(10,20,30))
# print(student.avg())


# Pass any number of arguments using *args

# class Student:
#     def __init__(self,name,*grades):
#         self.name = name
#         self.grades = grades

#     def avg(self):
#         return sum(self.grades)/len(self.grades)


# student = Student("Sunil",10,20,30)
# print(student.avg())

###### ============== str  ================= #####

# You will call the values in the object 

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __str__(self):
#         return f"Person {self.name} is {self.age} years old"

# person = Person("Sunil",24)
# print(person)


###### ============== repr  ================= #####

# you call the object itself to retrive tehe values !

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def __repr__(self):
#         return (f"<Person({self.name!r},{self.age})>")

# person = Person("Sunil",24)
# print(person)

###### ============== Inheritance  ================= #####

# class Person:
#     def __init__(self,fname,lname,age):
#         self.fname = fname
#         self.lname = lname
#         self.age = age
    
#     def printname(self):
#         print(self.fname,self.lname,self.age)

# # create a child class from Person

# class Student(Person):
#     pass

# student = Student("Sunil","Kumar",23)
# student.printname()

###### ============== Static and Class objects  ================= #####

# from datetime import date

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     # Create a person object by Birth
#     @classmethod
#     def birthYear(cls,name,year):
#         return cls(name,date.today().year-year)

#     # check if the person is adult or not
#     @staticmethod
#     def isAdult(age):
#         return age>18

# person1 = Person.birthYear('Sunil',2010)
# print(person1.age)

# if Person.isAdult(person1.age):
#     print ('Major')
# else:
#     print('Minor')
 