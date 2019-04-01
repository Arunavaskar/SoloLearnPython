# python is a object oriented language
# Almost everything in python is object orinted, with it's methods and properties 


# creating a class

class MyClass:
    x = 5
# create an object named p1, and print the value of x
p2 = MyClass()
print(p1.x)

# all classes have a function called __init__(), which is always
# initiated when the class is being initiated
# use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created


# create class name person, use the __init__() function to assign 
# values for name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("vaskar", 20)

print(p1.name, "is ", p1.age, "years old.")


# objects can also contain methods!

# insert a function that prints a greeting
# and executes on the p1 object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print("greetings", self.name)

p1 = Person("vaskar", 20)

print(p1.name, "is ", p1.age, "years old.")
p1.greeting
