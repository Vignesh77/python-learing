"""

@file       :count_lines.py
@brief      :Write a program to count no of lines in a text file.
@author     :vignesh

"""


count_line = 0

file_obj = open("hello.txt")
for line in file_obj.readline():
    count_line += 1
print "No of Lines :", count_line

