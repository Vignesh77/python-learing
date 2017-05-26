"""

@file       :plot_graph.py
@brief      :Write a program to count no of lines in n no of
            text files and  Plot it as a bar graph as File vs Lines.
@author     :vignesh

"""

import matplotlib.pyplot as plt
import os

list1 = []
file1 = []
total_file = input("how much file do u want to read :")
print "The file are..."
os.system("ls")
print "Enter the files names one by one"
for loop in range(total_file):
    file1.append(raw_input(""))

def line_count() :
    for loop in range(total_file):
        fp = open(file1[loop])
        count = 0
        for loop1 in fp.readlines():
            count += 1
        list1.append(count)

def bar_plot():
    list2 = [n for n in range(total_file)]
    plt.bar(list2, list1, align='center')
    plt.xticks(list2, file1)
    plt.show()


print file1
print list1
line_count()
bar_plot()
