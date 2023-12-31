# *args     = allows you to pass multiple non-key arguments
# **kwargs  = allows you to pass multiple keyword-arguments
#             * unpacking operator
#             1. positional 2. default 3. keyword 4. ARBITRARY


# The first example:

# def add(a, b):
#     return a + b
#
# print(add(1, 2))


# The second example:

# def add(*args):
#     # print(type(args))
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1, 2, 3, 6))


# The third example:

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
#
# display_name("Dr.", "Frank", "Chou", "zpy")


# The forth example of :"**kwargs"

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)
#     for key in kwargs.keys():
#         print(key)
#
# print_address(street = "123 Fake St.",
#               city = "Detroit",
#               state = "MI",
#               zip = "54321")

# The fifth example:
#
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# print_address(street = "123 Fake St.",
#               city = "Detroit",
#               state = "MI",
#               zip = "54321")

# The sixth one: use both args and kwargs here

# def shipping_label(*args, **kwargs):
#     # kwargs should followed by args
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end= " ")
#
# shipping_label("Dr.", "Frank", "Chou", "zpy",
#                street="123 Fake St.",
#                 city = "Detroit",
#                 state = "MI",
#                 zip = "54321")


# The seventh one:
def shipping_label(*args, **kwargs):
    # kwargs should followed by args
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('apt')} {kwargs.get('phone')}")
    # none phone
    print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")
    print(f"{kwargs.get('zip')}")

shipping_label("Dr.", "Frank", "Chou", "zpy",
               street="123 Fake St.",
                city = "Detroit",
               apt = "#100",
                state = "MI",
                zip = "54321")