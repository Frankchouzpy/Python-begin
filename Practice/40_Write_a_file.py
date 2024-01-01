# 'r' for read, and 'w' for write
# '\n' is for going down to a new line
# After you run this program, you should have a file named 'test.txe'
# within your project folder

# And if there is a existed file, it will overwrite your current file

# text = "You are now here:\nSo how fast can you type?\nI think it is very fast now!\nSo, you can do anything you want now!"
# appendent
#
# with open('test.txt', 'w') as file:
#     file.write(text)


# Also, you can append it, 'a' for append

text = "\nHave a nice day! See ya!"

with open('test.txt', 'a') as file:
    file.write(text)