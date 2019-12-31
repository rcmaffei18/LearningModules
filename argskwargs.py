'''
Demonstrates *args and **kwargs
'''


def fivepercenter(*args):
    '''
    Takes any number of arguments, sums and adds 5 fivepercenter
    Printing takes place within this
    *args is convention, but can use any variable name for this
    '''
    try:
        print(sum(args) * 1.05)
    except TypeError:
        print("You need to enter numbers")
    else:
        print("***************")


print("3, 4, 2, 6")
fivepercenter(3, 4, 2, 6)

print("3,4,5,6,73,7,888,54,5253")
fivepercenter(3, 4, 5, 6, 73, 7, 888, 54, 5253)

print("3, 4, c should return a ValueError")
fivepercenter(3, 4, "c")

print()
print("**************************")
print()


def myfunc(**kwargs):
    '''
    this function takes in any kwargs in a dictionary format
    can set any value you want for the key, followed by the
    corresponding value
    '''
    if 'fruit' in kwargs:
        print("My fruit of choice is {}".format(kwargs['fruit']))
    else:
        print("There is no fruit here")


myfunc(fruit='apple', veggie='lettuce')
myfunc(nut='peanut', veggie='lettuce')
print()
print('***********')
print()


def myfunc2(*args, **kwargs):
    '''
    Can also do both args and kwargs.  Args will be passed in via single
    inputs, while kwargs are added after in dictionary format.
    These must be entered in order, can't add more args to the end after kwargs
    '''
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0], kwargs['food']))


myfunc2(10, 20, 30, fruit='Orange', food='eggs', animal='dog')
