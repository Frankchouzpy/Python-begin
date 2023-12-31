# function = A block of reusable code
#            place () after the function name to invoke it

# The first example here:
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()
#
# happy_birthday("Bro", 20)
# happy_birthday("Steve", 23)
# happy_birthday("Frank", 48)

# The second example here:
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("FranChou", 42.5, "01/01")
# display_invoice("Frankchouzpy", 78.6, "10/25")

# The third example here:
# return = statement used to end a function
#          and send a result back to the caller
#
# def add(x, y):
#     z = x + y
#     return z
#
# def subtract(x, y):
#     z = x - y
#     return z
#
# def multiply(x, y):
#     z = x * y
#     return z
#
# def divide(x, y):
#     z = x / y
#     return z
#
# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1,2))
# print(divide(1, 2 ))

# The forth example here:
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("frank", "chou")

print(full_name)