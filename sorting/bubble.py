# Written small piece of code for sorting algorithm using bubble sort.

# Logic in using Bubble sort algorithm :
# Given an un-ordered list we compare adjacent elements in the list, each time putting right order of magnitude
# only two elements


unordered_list = ['8','4','2']

iteration_number = len(unordered_list)-1

for i in range(iteration_number):
    for j in range(iteration_number):
       if unordered_list[j] > unordered_list[j+1]:
           temp = unordered_list[j]
           unordered_list[j] = unordered_list[j+1]
           unordered_list[j+1] = temp
print(unordered_list)


