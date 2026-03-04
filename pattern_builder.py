class Pizza:
    def __init__(self):
        self.ingradients = []

    def add(self, item):
        self.ingradients.append(item)

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_cheese(self):
        self.pizza.add('cheese')

    def add_meat(self):
        self.pizza.add('meat')

    def build(self):
        return self.pizza

pizza = PizzaBuilder()
pizza.add_cheese()
pizza.add_meat()
print(pizza.build())