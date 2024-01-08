# ************************************************************************
# if __name__ == '__main__'
# ************************************************************************

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variavle a value of '__main__' if it's
# the initial module being run

# One:

# def main():
#     print("Hello!")
#
#
# if __name__ == '__main__':
#     main()


# Two:

# import Module_one
# print(__name__)
# print(Module_one.__name__)

# Three:

import Module_one

Module_one.hello()