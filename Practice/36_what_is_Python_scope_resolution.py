# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
# functions can't see inside of other functions

# The first example: Local
#
# Or different letters in functions
# def func1():
#     a = 1
#     print(a)
#
#
# def func2():
#     b = 2
#     print(b)
#
# func1()
# func2()

# The second example: Enclosed

def func1():
    x = 1
    def func2():
        x = 2
        print(x)

# func1()

# The third example: Global
#
# def func1():
#     x=1
#     print(x)
#
#
# def func2():
#     print(x)
#
# x = 3
#
# func1()
# func2()

# The last example: Built-in

from math import e   # Built-in

def func1():
    print(e)

e = 3  # Global

func1()
