# Listcomps No Longer Leak Their Variables
# list comprehensions, generator comprehensions and etc. now have their
# own local scope, like functions. Variables assigned within expression
# scope are local, but variables in the surrounding scope can still be
# referenced. Even better, the local variables do not mask the variables
# from the surrounding scope.
"""
>>> x = "ABC"
>>> dummy = [ord(x) for x in x]
>>> x
'ABC'
>>> dummy
[65, 66, 67]
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
