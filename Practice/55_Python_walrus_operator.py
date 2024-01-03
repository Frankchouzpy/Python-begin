# walrus operator :=
# new to  Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# One: The first you can code this and run it:

# happy = True
# print(happy)

# Two: But if you do this and run, it will show the TypeError :
# TypeError: 'happy' is an invalid keyword argument for print()

# print(happy = True)

# Three: So, you can run it by this, and run it. The result is 'Ture'.

# print(happy := True)

# Four: Now, here's a more practical example of why the walrus would be useful
# When you do the following codes

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#         if food == "quit"
#             break
#     foods.append(food)


#NOW, you can simple it as following:

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)

'''
The issue you're facing is due to the operator precedence in your code.
 The assignment expression (:=) has higher precedence than the comparison
  (!=) operator. As a result, the assignment is applied to the result of
   the comparison, leading to unexpected behavior.
To fix this issue, you should use parentheses to explicitly define 
the order of operations. Here's the corrected code:

By adding parentheses around (food := input("What food do you like?: ")),
 you ensure that the assignment is done correctly before comparing the value
  to "quit." This will correctly store the user's input in the foods list 
  and print the list of foods as expected.
'''