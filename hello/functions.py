
def myFunc(arg1, arg2, arg3 = 6):
    return arg1 + arg2 + arg3

print myFunc(1,2,3)
print myFunc(arg2 = 2, arg1 = 1)
print myFunc(arg2 = 2, arg1 = 1, arg3 = 3)