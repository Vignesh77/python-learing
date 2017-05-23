"""
@file       :list_add.py
@brief      :Create the list and add the elements.
@author     :vignesh

"""
list_len = input("Enter the length of list :")
input_list =[ ]
print "Enter the values to list"
for index in range(list_len) :
    list1 = input("")
    input_list.append(list1)
print input_list
print "Enter do u want to add values in list"
print "yes or no"
usr_opt =raw_input("")
if usr_opt == 'yes' :
    print "Enter the index and value"

    index =input("")
    value =input("")
    if index > len(input_list) :
        print "Invalid option"
    input_list.insert(index,value)
print input_list
