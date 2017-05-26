"""
@file       :reduce_sum.py
@brief      :Calculating sum of numbers from 1-100 using reduce()
@author     :vignesh
"""


def fun(data, data1):
    """
    print sum of numbers from 1 to 100
    """
    return data + data1

print reduce(fun, range(1, 101))








