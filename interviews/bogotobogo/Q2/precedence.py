# NOT has first precedence, then AND, then OR.

print(True or False and False)
print(not True or False or not False and True)
