class Car:

    color = "red"


class Motorcycle:

    color = None

'''
Now make sure when you define this function, it's not within the 'car' class,
then technically this would be a method fo the 'car' class what we would like is
a separate function outside of the 'car' class.
'''


def change_color(vehicle, color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

# change_color(car_1, "red")
# change_color(car_2, "white")
change_color(car_3, "blue")
change_color(bike_1, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)