 # default arguments = A default value for certain parameters
 #                    default is used when that argument is omitted
 #                    make your fuctions more flexible, reduces # of arguments
 #                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# The first example:
# def net_price(list_price, discount, tax):
#      return list_price * (1 - discount) * (1 + tax)
#
# print(net_price(500, 0, 0.05))

# The second example:
# def net_price(list_price, discount = 0, tax = 0.05):
#      return list_price * (1 - discount) * (1 + tax)
#
#
# print(net_price(500))

# The third example:
# def net_price(list_price, discount=0, tax=0.05):
#      return list_price * (1 - discount) * (1 + tax)
#
#
# # print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0.06))

# The forth example:

import time

# def count(start, end):
#     for x in range(start, end +1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
#
# count(0, 10)

# The fifth example:

import time

def count(end, start = 0):
# Non-default argument follows defualt argument
    for x in range(start, end +1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(10)
count(30, 28)