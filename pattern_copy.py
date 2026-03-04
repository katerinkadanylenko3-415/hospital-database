import copy

class Car:
    def __init__(self, model, colour):
        self.model = model
        self.colour = colour

    def clone(self):
        return copy.copy(self)

prototype_car = Car("Tesla", "blue")
cloned_car = prototype_car.clone()
print("Driginal car: ", prototype_car)
print("cloned car: ", cloned_car)

