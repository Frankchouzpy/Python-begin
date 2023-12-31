# module = a file containing code you want to include in your program
#           use 'import' to include a module (built-in or your own)
#           useful to break up a large program resuable separate files
# print(help("modules"))
# print(help("math"))

# import math
# print(math.pi)

# import math as m
# print(m.pi)

# from math import pi
# print(pi)

import example
# I have built a module named 'example' in the 35th practice in the same folder

# result = example.pi
result =example.square(3)
result =example.cube(3)
result =example.area(3)
result =example.circumference(3)

print(result)