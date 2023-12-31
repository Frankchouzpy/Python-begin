# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1.positional 2. default 3. KEYWORD 4. arbitrary

# The first example:

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
#
# hello("Hello", "Mr.", "Frank", "Chou")

# The second example:

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
#
# hello("Hello", first="Frank", last="Chou", title="Mr.")


# The forth example:
# The "end" is a keyword argument

# for x in range(1, 11):
#     print(x, end=" ")

# The fifth example:
# The "sep" is an another keyword argument here:

# print("1", "2", "3", "4", "5", sep="-")

# The sixth example:

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=456, last=7890)
phone_num = get_phone(1, 123, 456, 7890)
print(phone_num)