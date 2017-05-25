"""
@file       :divide_by_zero.py
@brief      :Print 'Can not divide' when 100/0
@author     :vignesh

"""


def divide_zero(number1, number2):
    """
    can not divide by zero
    """
    try:
        print number1 / number2
    except ZeroDivisionError:
        print "Cannot divide by zero"

divide_zero(100, 0)
