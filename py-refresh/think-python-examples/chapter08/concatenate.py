# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#   print letter + suffix
# The output is:
# Jack
# Kack
# Lack
# Mack
# Nack
# Oack
# Pack
# Qack
# Of course, that’s not quite right because “Ouack” and “Quack” are misspelled.

# Exercise 8.2 Modify the program to fix this error.


prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
  if letter == "O" or letter == "Q":
    print(letter+'u'+suffix)
  else:
    pass
  print(letter + suffix)