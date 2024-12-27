class Car:
    color = "Blue"
    on = False

    def sayName(self):
        print("A car")

    def description(self):
        message = f"A car with a color: {self.color} and is turn on: {self.on}"
        return message

    def message(self):
        print("+" * 10)
        print(self.description())
        print("+" * 10)


car = Car()
print(car.color)
print(car.on)
car.sayName()
print(car.description())
car.message()
