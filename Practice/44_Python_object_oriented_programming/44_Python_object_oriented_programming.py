# Python object oriented programing, also known as poop.
# you can do that in this file:

# class Car:
#     pass

# So if you have a small program, it may be better to write your
# class within your main module.

# But if your class is fairly large, you may want to consider placing your
# class within a separate module

# So if you were to take that route, we would go to 'file'-'new python file' and
# we will name this car, and we would declare our class within the separate module

from car import Car

car_1 = Car("Chevy","Corvetter",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()
