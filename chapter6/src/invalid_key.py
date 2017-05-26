"""
@file       :invalid_key.py
@brief      :Print 'Invalid key!' when d['os_ver'] on d={'os':'linux'}
@author     :vignesh

"""

dict1 = {'os':'linux'}

def checking_key(dict2):
    """
    function for checking key in dict
    """
    try:
        print dict2['os_var']
    except KeyError:
        print "invalid key"

checking_key(dict1)
