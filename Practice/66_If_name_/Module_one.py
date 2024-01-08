# ************************************************************************
# if __name__ == '__main__'
# ************************************************************************

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within  __name__

# Python will assign the __name__ variavle a value of '__main__' if it's
# the initial module being run

# One:
# print(__name__)


# Two:

# import Module_two
# print(__name__)
# print(Module_two.__name__)



# Three:

# if __name__ == '__main__':
#     print("running this module directly")
# else:
#     print("running other module indirectly")


#Four:


def hello():
    print("Hello!")

# if __name__ == '__main__':
#     hello()

if __name__ == '__main__':
    hello()
