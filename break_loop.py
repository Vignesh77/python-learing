"""
@file       :break_loop.py
@brief      :Write the program to break the loop if user give 'n' as input, if 'y' continue.
@author     :vignesh(vignesh.nanjundan@vvdntech.in)

"""
while True :
    print "Enter the option.."
    print "y ->continue "
    print "n -> break"
    option =raw_input("")
    if option == 'y' :
        continue
    else :
        break

