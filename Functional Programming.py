# this function takes two args, "func" and "arg"
def apply_twice(func, arg):
    # here arg gets a value, which gets passed to func and then again to the outer most part, func again!
    return func(func(arg))

# gets one arg x
def add_five(x):
    # returns a value of x added to 5
    return x + 5

# here apply_twice() takes two params, one is the function add_five() and another is 10
print(apply_twice(add_five, 10))

# what heppens here is when running 12th line
# apply_twice(add_five, 10)
#   return add_five(add_five(10)
#   now add_five works with 10
#add_five(10)
#   return 10 +5
# and this gets repeated once more as apply_twice returns add_five(add_five(10))
# so the inner section gets done, then the outer section which is basically repeatation of the same code!    