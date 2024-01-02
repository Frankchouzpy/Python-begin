# The first method here:

# import os
# os.remove('C:\\Users\\24154\\PycharmProjects\\helloworld\\42_Move_a_file\\move.txt')

# The second one:

# import os
#
# path = "C:\\Users\\24154\\PycharmProjects\\helloworld\\42_Move_a_file\\move"
#
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("That file was not found!")
# except PermissionError:
#     print("You do not have permission to delete that!")


# The third one, how to delete a folder:

# import os
# import shutil
#
# path = "C:\\Users\\24154\\PycharmProjects\\helloworld\\42_Move_a_file\\move"
# # input your file/folder path
#
# try:
#     os.rmdir(path)
# except FileNotFoundError:
#     print("That file was not found!")
# except PermissionError:
#     print("You do not have permission to delete that!")
# except OSError:
#     print("You can not delete that using that funcion")
# else:
#     print("{path}" + " was deleted!")


# The forth one, using the 'shutil' function to delete a
# folder which containing a file/files.
# NOTICE: It will delete a directory and all files contained within!

import os
import shutil

path = "C:\\Users\\24154\\PycharmProjects\\helloworld\\42_Move_a_file\\move"
# input your file/folder path

try:
    shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("You do not have permission to delete that!")
except OSError:
    print("You can not delete that using that funcion")
else:
    print("{path}" + " was deleted!")