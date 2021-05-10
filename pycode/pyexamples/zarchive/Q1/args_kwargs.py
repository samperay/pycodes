# We may want to use *args when we're not sure how many arguments might be passed to our function,
def print_all(*args):
    for x in enumerate(args):
        print(x)
print_all('A','a','B','b')

# The keyword arguments is a special name=value syntax in function calls that specifies passing by name.
# It is often used to provide configuration options.

def kargs_func(**kargs):
    for k,v in kargs.items():
        print(k,v)

kargs_func(**{'uno':'one','dos':'two','tres':'three'})
