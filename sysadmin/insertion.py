# this code is for the insertion sort

#logic: we might assume certain part of the list is already being sorted, while remaining other
#is unsorted. we move through the unsorted portion of the list, picking one element at a time.
#With this element, we go through the sorted portion of the list and insert it in the right order
#so that the sorted portion of the list remains sorted

unsorted_list = ['5','4','2']

for index in range(1, len(unsorted_list)):
    search_index = index
    insert_value = unsorted_list[index]

    while search_index > 0 and unsorted_list[ search_index -1] > insert_value :
        unsorted_list[search_index] = unsorted_list[ search_index -1]
        search_index -= 1

    unsorted_list[search_index] = insert_value

print(unsorted_list)
