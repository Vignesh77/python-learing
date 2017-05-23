"""
@file       :convert_list_str.py
@brief      :Write the program to convert all the elements of list
            :into string
@author     :vignesh(vignesh.nanjundan@vvdntech.in)

"""
list1 = [ 1, 2, 3, 4, 5 ]
string ="".join(str(x) for x in  list1)
print string
print type(string)
