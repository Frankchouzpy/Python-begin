# exception = events detected during execution that interrupt the flow of a program

# The first example here:
# Example one:
# numerator = int(input("Enter a number to divide: "))
# denomiator = int(input("Enter a number to divide by: "))
# result = numerator / denomiator
# print(result)

# In the example one , if 5 / 0,  ZeroDivisionError: division by zero
# So we can use the "try" and "except" to show whether there is a wrong:

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denomiator = int(input("Enter a number to divide by: "))
#     result = numerator / denomiator
#     print(result)
# except Exception:
#     print("Someting went wrong!")

# Or another "except":

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denomiator = int(input("Enter a number to divide by: "))
#     result = numerator / denomiator
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero! idiot!")


# And if you enter "5 / ip", Error: ValueError: invalid literal for int() with base 10: 'ip'
# So how to solve it:

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denomiator = int(input("Enter a number to divide by: "))
#     result = numerator / denomiator
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero! idiot!")
# except ValueError:
#     print("Enter only numbers plz!")


# And we can print the exceptions:

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denomiator = int(input("Enter a number to divide by: "))
#     result = numerator / denomiator
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero! idiot!")
# except ValueError as  e:
#     print(e)
#     print("Enter only numbers plz!")
# except Exception as e:
#     print(e)
#     print("Something went wrong!")

# And we can calculate the result in the end, and add a "finally":

try:
    numerator = int(input("Enter a number to divide: "))
    denomiator = int(input("Enter a number to divide by: "))
    result = numerator / denomiator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as  e:
    print(e)
    print("Enter only numbers plz!")
except Exception as e:
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally:
    print("This will always execute!")
