# In this practice, I'm going to explain how we can read the
# contents of a fiele using pytion

# List the name of your file or the file path
# I use the file name cause this file of mine is within
# my project folder!
# If your file is someplace else, you'll probably need the file path

#NOTICE: On Windows, Python often defaults to the 'GBK' encoding for reading
# files, which can cause problems if your file is encoded differently
# (like in UTF-8). So "encoding='utf-8'"

# with open('test.txt') as file:
try:
    with open("C:\\Users\\24154\\PycharmProjects\\helloworld\\test.txt",
              encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!")
print(file.closed)