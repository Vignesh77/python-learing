"""
@file       :print_letter.py
@brief      :Print the letters from 'gnu-linux is rule the world now'.
@author     :vignesh(vignesh.nanjundan@vvdntech.in)

"""
string = "gnu-linux is rule the world now"
for letter in string :
    if (((letter >= 'a') and (letter <= 'z')) or ((letter >= 'A') and (letter <= 'Z'))):
        print letter
