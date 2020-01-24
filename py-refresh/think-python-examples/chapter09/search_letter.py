# def has_no_e(word):
#   for letter in word:
#     if letter == 'e':
#       return False
#   return True

# print(has_no_e('Sunidel'))

def avoid(word,letter):
  for item in word:
    if letter in item:
      return True
  return False

print(avoid("Sunil",'g'))