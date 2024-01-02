class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
# 'self' is referring to the object that we're currently working on or creating

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+"  is stopped")