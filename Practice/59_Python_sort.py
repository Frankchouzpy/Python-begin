# sort() method   = used with list
# sort() function = used with iterables

# students = [("squidward", "F", 60),
#             ("Frank", "A", 33),
#             ("Heisenberg", "B", 20),
#             ("Patrick", "D", 36),
#             ("Mr. Krabs", "C", 78)]

# grade = lambda grades:grades[1]
# age = lambda ages:ages[2]


# students.sort(reverse=True)
# students.sort()
# students.sort(key=age)
# students.sort(key=grade)
# students.sort(key=grade, reverse=True)

students = (("squidward", "F", 60),
            ("Frank", "A", 33),
            ("Heisenberg", "B", 20),
            ("Patrick", "D", 36),
            ("Mr. Krabs", "C", 78))

age = lambda ages:ages[2]

# sorted_students = sorted(students, reverse=True)
sorted_students = sorted(students, key=age)

# for i in sorted_students:
for i in sorted_students:
    print(i)