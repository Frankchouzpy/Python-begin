# Higher Order Function = a function that either:
#                             1. accept a function as an argument
#                                 or
#                             2. return a function
#                             (In Python, functions are also treated as objects)


# The first example


# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
#
# hello(loud)
# hello(quiet)


# The second example

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))