# Zero division error example

num1 = 1
num2 = 0
num1 / num2


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

except:
    print("an error occured")
    raise
# This code will run no matter what!
# finally statement even runs if an uncaught exception occurs in one of the preceding block
else:
    print("congo there was no exceptions!")
finally: 
    print("You need to correct the code if it didn't run previously or if it did, congo")



# if the given condition in assertion block is true, the args messege excutes, if false, the code stops there and prints the arg messege
print("checking assertion")
# check if 1 is greater than 2, if not print the messege
assert 1>2, "1 isn't greater than 2!"
