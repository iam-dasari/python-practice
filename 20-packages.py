# A Package is a way of structuring Python's module namespace by using "prints" dotted module names. 
# A package is a collection of Python modules under a common namespace. 
# A directory must contain a special file called __init__.py in order for Python to consider it as a package. 
# This file can be empty, and it indicates that the directory it is present in is a Python package,
#  so it can be imported the same way a module can be imported. 
# A package can contain sub-packages, which are simply packages nested inside another package.
# A package can also contain modules, which are simply Python files that contain code.
# A package is a folder that contains a special file called __init__.py, which tells Python 
# that the folder is a package.

from Library import add, sub

add = add.addition(10, 20)
print(add)
sub = sub.subtraction(10, 20)
print(sub)