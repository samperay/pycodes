##### ============== Simple function call ================= #####

# def main():
#     print("Hello World..")

# main()

##### ============== function returning values  ================= #####

# def sum(x,y=10): # default value being set and no need to pass any argument in calling parameter
#     return x+y

# result = sum(10)
# print(result)

##### ============== fLocal and Global scope of variables  ================= #####
 
# y=2  # this will be used when you haven't passed any argument in the local define calling
# def sum(x,y=y): 
#     return x+y

# result = sum(10,5)
# print(result)

##### ============== lambda functions  ================= #####

# Lambdas are just functions without a name.
# They are used to return a value calculated from its parameters.
# Almost always single-line, so don't do anything complicated in them.
# Very often better to just define a function and give it a proper name.

# add = lambda x,y: x+y
# print(add(2,3))

# sequence = [1, 3, 5, 9]
# doubled = map(lambda x: x * 2, sequence)
# print(list(doubled))

##### ============== Dictionary Comprehensions  ================= #####

# users = [
#     (0, "Bob", "password"),
#     (1, "Rolf", "bob123"),
#     (2, "Jose", "longp4assword"),
#     (3, "username", "1234"),
# ]

# # you would be required to map the name to the id else it would require a long loops to retrive the data

# username_mapping = { user[1]: user for user in users }
# userid_mapping =   { user[0]: user for user in users }

# print(username_mapping)
# print(userid_mapping)

# username_input = input("Enter your username: ")
# password_input = input("Enter your password: ")

# _, username, password = username_mapping[username_input]

# if password_input == password:
#     print("Your details are correct!")
# else:
#     print("Your details are incorrect.")


##### ============== Un-packing arguments  ================= #####

# def print_numbers(*args):
#     print(args)

#     squarelist = []
#     squarelist = [ x*x for x in args]
#     print(squarelist)

# print_numbers(1,2,4)

##### ============== Un-packing keywords  ================= #####

# def named(**kwargs):
#     print(kwargs)

def print_nicely(**kwargs):
    #named(**kwargs)  # Unpack the dictionary into keyword arguments.
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)