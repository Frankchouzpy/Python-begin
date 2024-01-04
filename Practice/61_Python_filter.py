# filter() = creates a collection of elements from an iterable for which
# a function returns ture.
# filter(function, iterable)

friends = [("Rachel", 19),
           ("Monica", 18),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Frank", 20),
           ("Ross", 21)]

age = lambda date:date[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)