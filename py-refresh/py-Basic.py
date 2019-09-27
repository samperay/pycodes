#!/usr/bin/python

# # variables, string formatting
# x=10
# y=1.2
# first_name = "Sunil"
# last_name = "kumar"

# print("x:",x,"y:",y)

# # string formatting
# print(first_name)

# greeting = "Hello, {}"
# greeting_name = greeting.format(first_name)
# print(greeting_name)

# # string concatenation
# full_name = first_name+ " " + last_name
# print(full_name)

# # Getting userinput to pring name/integres
# message = input('Enter your firstname: ')
# first_name = str(message)


# first_value = input ('Enter first Number: ')
# value1 = int(first_value)

# # first type of print value 
# print("------ first way of printing--------")
# print("you have entered name as:", first_name)
# print("Entered value is:",value1)

# # secode type of print using formatted
# print('--------- second way of printing using formatters-----')
# print(f"{first_name}","is the value you have entered using keyboard")
# print(f"{value1}", "was the value you have entered")

# # simple math calculations 
# print("\n")
# message = input("Enter your age:" )
# age = int(message)

# months = age * 12

# print(f"your age {age} means , you are {months} months old")

# # Basic about list, tuples, sets 
# print("\n")

# l = ["Sunil","Kumar","Amperayani"]
# t = ("Sunil","Kumar","Amperayani")
# s = {"Sunil","Kumar","Amperayani"}

##### ============== List Operations ================= #####
# # you can change value in the list, append, duplicate, and modify values as well
# print("\n List Ops")
# print("Item in list:",l[0])
# l.append('Bob')
# print(l)
# l[0]="Sun"
# print(l)
# l.append('Sunil')
# l.append('Sunil')

# for item in l:
#     print(f"{item}")

##### ============== Tuple Operations ================= #####
# # tuple are immutable so you cannot change values, also you cannot add values tooo
# print("\n Tuple Ops")
# print(t[0])
# print(t)


##### ============== Set Operations ================= #####
# print("\n set Ops")
# print(s)
# # you cannot do as set are un-ordered ane hence it wont work !
# #print(s[0])
# #s[0] = 'Sun'
# s.add('Bob')
# print(s)
# s.add('Sunil')
# print(s)

##### ============== Advance set Operations ================= #####

# indians = {"Amar","Akbar","Antony"}
# abroad = {"Amar","John"}

# local = indians.difference(abroad)
# print(local)

# # Union of two sets 
# friends = indians.union(abroad)
# print(friends)

# # Intersection of two sets 
# common_friends = indians.intersection(abroad)
# print(common_friends)

##### ============== Booleans ================= #####
# set1 = {"Sun", "Moon"}
# set2 = {"Sun", "Moon"}
# print( set1 == set2 )

# if set1 == set2:
#     print('Both sets are equal')
# else:
#     print('Both are un-equal sets')

# if 'Amar' in indians:
#     print("'Amar' has been found in set")
# else:
#     print("'Amar' Not found")

##### ============== loops ================= #####

# friends = ["Sunil","Kumar"]
# grades = [35, 67, 98, 100, 100]
# # for i in friends:
# #     print(i)

# count=0
# count = len(friends)-1
# while count >=0:
#     print(friends[count])
#     count=count-1

# print(sum(grades))
# print(sum(grades)/len(grades))

# sum=0
# for i in grades:
#     sum=sum+i 
# print(sum)

##### ============== List Comprehensions ================= #####

## without list compresention
# for i in numbers:
#     result = i * i
#     sqrnumbers.append(result)

# print(sqrnumbers)

# numbers = [1,2,3,4,5]
# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]

# sqrnumbers = [ x*x for x in numbers]
# evennumbers = [ x for x in numbers if x%2==0]
# oddnumbers = [ x for x in numbers if x%2!=0]
# print("square numbers: ",sqrnumbers)
# print("Even Numbers: ",evennumbers)
# print("Odd Numbers: ",oddnumbers)

# friends_s = [friend for friend in friends if friend.startswith('S')]
# print(friends_s)

##### ============== Dictionaries ================= #####

# # -- List of dictionaries --

# friends = [
#     {"name": "Rolf Smith", "age": 24}, # 0 the record
#     {"name": "Adam Wool", "age": 30}, # 1
#     {"name": "Anne Pun", "age": 27}, # 2
# ]
 
# for friend in friends:
#     for name,age in friend.items():
#         print(f"{ name } {age }",end=' ')
#     print("\n")    


##### ============== Blank Variable outputs ================= #####
# person = ("Bob", 42, "Mechanic")
# name, _, profession = person

# print(name, profession)  # Bob Mechanic

##### ============== Mutability ================= #####


# a = []
# b = a

# # Remember a and b are _names_ for the list. They both have the _same_ value.
# a.append(35)  # Modify the value.

# print(a)
# print(b)

# # Here they are different lists, because [] creates a new list every time. You can check whether two things are the _same_ one by usingt the `id()` function:

# print(id(a))
# print(id(b))  # Different from id(a)

# -- immutable --

# Some values can't be changed because they don't have methods that modify the value itself.
# In case of the list, `.append()` mutates the list.
# For example integers don't have any such methods, so they are called _immutable_.

# a = 8597
# b = 8597

# print(id(a))
# print(id(b))  # Same one

# a = 8598

# print(id(a))
# print(
#     id(b)
# )  # Different, because we didn't change 8597. We just used the name 'a' for a different value. 'b' still is a name for 8597.

# # Most things are mutable in Python. If you want to keep one of your classes immutable, don't add any methods that change the objects' properties.

# # Tuples and strings are the only fundamental collection in Python which is immutable.
# # Lists, sets, dictionaries are all mutable.
# # Integers, floats, and booleans are all immutable.
