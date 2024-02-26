#Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
def do_twice(f, s):
    f(s)
    f(s)
def print_twice(s):
    print(s)
    print(s)
    
def do_four(f, s):
    do_twice(f, s)
    do_twice(f, s)
    
do_twice(print, 'spam')
print('')
do_four(print, 'spam')
