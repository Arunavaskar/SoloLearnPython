# Zero division error example

#num1 = 1
#num2 = 0
#num1 / num2


# Exception handling

# This try block takes a piece of code
try:
    num3 = 3
    num4 = 0
    print(num3/num4)
# if the code results a particular error
# this except block will have to have that possible error type name in the block
except ZeroDivisionError: # except_ION
    # and wil return a desired output!
    print("Fuck, an error occured!")
    print(num3, " was num3 and ", num4, "was num4\nthey were devided by each other and caused a zero division error!")

        