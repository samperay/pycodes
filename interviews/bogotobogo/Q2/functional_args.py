# arg2 aggregates the rest of args into a tuple

def getThem(arg1, *arg2):
   print(type(arg1),type(arg2), arg2)

getThem('uno','dos','tres','cuatro','cinco')

# arg2 aggregates the remaining parameters into a dictionary.
def getThem1(arg1, **arg2):
   print(type(arg2), arg2)

getThem1('numbers',one='uno',two='dos',three='tres',four='cuatro',five='cinco')

# Unpacking args
# this code will not work as there is typeError - missing arguments
#TypeError: getThem() takes exactly 5 arguments (1 given)
def getThem2(a,b,c,d,e):
   print(a,b,c,d,e)

mList = ['uno','dos','tres','cuatro','cinco']
print(getThem2(*mList))

# above code should be chaged as below
# getThem(*mList)
# *mList will unpack the list into individual elements to be passed to the function.
