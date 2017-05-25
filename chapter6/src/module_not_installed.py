"""
@file       :module_not_installed
@brief      :Print 'Module not installed' when 'import gnulinux'
@author     :vignesh

"""


def checking_module():
    """
    function to check whether module is
    installed or not
    """
    try:
        import gnulinux
        print "module is installed"
    except ImportError:
        print "Module not installed"

checking_module()
