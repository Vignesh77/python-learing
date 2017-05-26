"""
@file       :change_odd_string.py
@brief      :Write the program to replace the odd position string
            :with 'X' on any strings.
@author     :vignesh(vignesh.nanjundan@vvdntech.in)

"""
total_string = input("How much string do u want to enter :")
str_list = [ ]
print "Enter the strings one by one.."
for index in range(total_string) :
    ip_str = raw_input("")
    str_list.append(ip_str)
print "The input strings are.."
print str_list
for index in range(total_string) :
    if index % 2 != 0 :
        str_list[index] = 'X'
print "The expected output is"
print str_list
