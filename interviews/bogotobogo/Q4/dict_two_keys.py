first = ["Mary", "James", "Thomas", "William", "Elizabeth"]
last = ["Li", "O'Day", "Miller", "Garcia", "Davis"]

name_dict = dict(zip(first, last))

# sort the dictionary using two keys :
# the key tuple used is (len(last), first)
name_list = sorted(name_dict, key = lambda k: (len(name_dict[k]), k))

for item in name_list:
    print(item, name_dict[item])
