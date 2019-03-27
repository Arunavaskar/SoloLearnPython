# lambda expression or say lambda function where x is the argument
triple = lambda x: x * 3

# this is another lambda expression where there are 2 arguments, x and y
add = lambda x, y: x + y

# here under the print function add lambda gets called where there are two parameters passed as opposed to the 2 arguments
print(add(triple(3), 4))
