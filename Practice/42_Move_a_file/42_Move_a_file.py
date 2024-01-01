import os

source = "test.txt"
destination = "C:\\Users\\24154\\PycharmProjects\\helloworld\\path\\move.txt"
# 'test.txt' also can be a path, and destination can be the path you want to move to

try:
    if os.path.exists(destination):
        print("There is already a file there!")
    else:
        os.replace(source, destination)
        print(source + " was moved!")

except FileNotFoundError:
    print(source + " was not found!")
