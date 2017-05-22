"""
@file   :find_sub_string.py
@brief  :Return the number of times that the string "code" appears
        :anywhere in the given string, except we'll accept any
        letter for the 'd', so "cope" and "cooe" count.
        count_code('aaacodebbb') =  1
        count_code('codexxcode') =  2
        count_code('cozexxcope') =  2
@author :vignesh

"""
def find_sub_string(string) :
    count = 0
    for i in range(len(string)) :

        if string[i] == 'c' :
            if i+3 <= len(string) :

                if string[ i+1] =='o' and string[ i+3] =='e' :
                    count += 1
    print count
find_sub_string("codexxcope")

