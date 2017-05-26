"""
@file       :map.py
@brief      :Convert all the numbers between 1-100 as string using map.
@author     :vignesh
"""


def fun(number):
    """
    function for coverting number
    into string
    """
    return str(number)

print map(fun, range(1, 101))
