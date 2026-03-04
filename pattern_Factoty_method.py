class Car:
    pass

class BMW(Car):
    pass

class Audi(Car):
    pass

class Mbo(Car):
    pass

def car_factory(brand):
    if brand == 'BMW':
        return BMW()
    elif brand == 'Audi':
        return Audi()
    elif brand == 'Mbo':
        return Mbo()
    else:
        raise ValueError('Unknown brand')

car1 = car_factory("BMW")
car2 = car_factory("Audi")