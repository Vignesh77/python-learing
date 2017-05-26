"""
@file       :dict_comp.py
@brief      :Create the dictionary dict_sample = {1:1, 2:2} using
            dictionary comprehension
@author     :vignesh
"""
def print_dict():
    """
    function for creating dictionary
    comprehension
    """
    dict1 = {n:n for n in range(1, 11)}
    print dict1

print_dict()
