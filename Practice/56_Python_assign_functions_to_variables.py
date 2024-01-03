# When you defined a funchion and recalled it , you need to add '()'

def hello():
    print("Hello")

# hello() # The set of parentheses that comes after a function's name is the portion
#         # that well call the function. If you remove it, we would not in fact call
#         # that function

# if I want to show you if I was to print the name of the function Hello, what would
# be displayed is the memory address of this function.

# print(hello)

# And if I assign Hello to a variable:

hi = hello
# print(hi)

# And call the hi:

hi() # It seems that the function has two names Hello and hi!

# Now we can do something like this:

say = print
say("Whoa! I can't believe you have learnt this! You are 你小子！")



