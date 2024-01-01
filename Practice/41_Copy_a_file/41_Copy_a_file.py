# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)
# To use the three functions, you could import the 'shutil' modile

import shutil

shutil.copyfile("test.txt", 'copy.txt')   #src,dst: source and destination
# rename 'test.txt' to 'copy.txt'
# And 'test.txt' and 'copy.txt' can be a path you want it to be
# Then may you have guess that you can change 'copyfile' to 'copy' or 'copy2'
