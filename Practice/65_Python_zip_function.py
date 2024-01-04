# zip(*iterables) = aggregare elements from two or more iterable (list, tuple,sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element.

usernames = ["Dude", "Frank", "你小子"]
passwords = ("p@ssword", "abc123", "guest")

#----------------------------------------------------

# # users = zip(usernames, passwords)
#
# users = list(zip(usernames, passwords))
#
# for i in users:
#     print(i)
#
# print(type(users))

#----------------------------------------------------

# users = dict(zip(usernames, passwords))
#
# print(type(users))
#
# for key, value in users.items():
#     print(key+" : "+ value)

#----------------------------------------------------

login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)