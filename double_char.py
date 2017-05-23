"""
@file       :double_char.py
@brief      :Given a string, return a string where for every char
            in the original, there are two chars.
            Eg.   double_char('The') = 'TThhee'
@author     :vignesh

"""

def double_char(string) :
    list1 = []
    for i in string:
        for j in range(2) :
            list1.append(i)
    return "".join(list1)


string = double_char("THE")
print string 






