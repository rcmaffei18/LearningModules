def new_decorator(original_func):
    '''
    This takes in a function.  First, it prints the jazz line
    then it runs the function it took in, then it runs the extra
    code line
    Finally, it returns the entire thing
    '''
    def wrap_func():
        print('Some extra jazz happening here')

        original_func()

        print('Some extra code, after original function')

    return wrap_func

def func_needs_decorator():
    '''
    This is just a simple method which prints a single line
    It will be taken into the new_decorator function
    '''

    print("I want to be decorated")

func_needs_decorator()

print("Everything after this happens through the decorator")
print("**************************")

@new_decorator # Here, you are assigning the new decorator on top
def func_needs_decorator():
    print("I want to be decorated")

func_needs_decorator() # Running this runs everything because of the @ part
