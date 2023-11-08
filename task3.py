class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("The car is started")

    def stop(self):
        print("The car is turned of")

    def set_year(self, year):
        self.year = year

    def set_type(self, car_type):
        self.car_type = car_type

    def set_color(self, color):
        self.color = color


car = Car("Blue", "Sedan", 2021)
car.start()
car.stop()

print("Year of issue:", car.year)
print("Car type:", car.car_type)
print("Car color:", car.color)






