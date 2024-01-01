import  os

# If you have the backslashes in your file path like this:
# C:\Users\24154\PycharmProjects\helloworld\main.py
# You'll probably need double backslashes because
# that's the escape sequence for a backslash within a string:
# C:\\Users\\24154\\PycharmProjects\\helloworld\\main.py

# path = "C:\\Users\\24154\\PycharmProjects\\helloworld\\main.py"
#
# if os.path.exists(path):
#     print("That location exists!")
# else:
#     print("That location doesn't exist!")

# And how to show the path is a file or not:

path = "C:\\Users\\24154\\PycharmProjects\\helloworld\\Practice"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That's is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")

else:
    print("That location doesn't exist!")
