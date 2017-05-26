"""
@file       :odd_num.py
@brief      :Print odd number between 1-100 using list comprehension
@author     :vignesh
"""
def print_odd_num():
    """
    function for printing odd
    numbers from 1 to 100
    """
    list1 = [num for num in range(1, 101, 2)]
    print list1

print_odd_num()
