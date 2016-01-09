def print_compare(func1, func2, *args):
    '''
    Prints the name and output of 2 functions to easilly compare outputs via forloop
    Assumes both functions return values and that they take the same arguments
    When calling, don't put () for func1 or func2
    '''
    print("args:", args , "|" , func1.__name__ + ":", func1(*args), "|", func2.__name__ + ":", func2(*args))

def identity(*x):
    return x

def empty(x):
    pass
