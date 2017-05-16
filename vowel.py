"""
# @file         :vowels.py
# @brief        :Write the program to print vowels and consonant letter
#               from 'gnulinux'
#@author        :vignesh(vignesh.nanjundan@vvdntech.in)

"""

string1 = 'gnulinux'
#To finding vowel letter
print " vowels are "
for loop in range(0, len(string1)):
    if ((string1[loop] == 'a') or (string1[loop] == 'e') or
            (string1[loop] == 'i') or (string1[loop] == 'o') or
            (string1[loop] == 'u')):
        print string1[loop]
#To finding consonant letters
print "consonant letters are"
for loop in range(0, len(string1)):
    if ((string1[loop] != 'a') and  (string1[loop] != 'e') and
            (string1[loop] != 'i') and (string1[loop] != 'o') and
            (string1[loop] != 'u')):
        print string1[loop]

