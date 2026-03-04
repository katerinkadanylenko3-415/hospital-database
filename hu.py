class Order:
    def __init__(self, items):
        self.items = items  # список цін

    def total_price(self):
        return sum(self.items)


class Discount:
    def apply(self, price):
        return price


class NoDiscount(Discount):
    pass


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, price):
        return price * (1 - self.percent / 100)


class PriceCalculator:
    def __init__(self, discount: Discount):
        self.discount = discount

    def calculate(self, order: Order):
        return self.discount.apply(order.total_price())


class InvoiceGenerator:
    def generate(self, order: Order, total_price):
        print("----- РАХУНОК-ФАКТУРА----")
        print("Товари:", order.items)
        print("Сума до оплати:", total_price)
        print("--------------------------")


class OrderStorage:
    def save(self, order: Order):
        pass


class FileOrderStorage(OrderStorage):
    def save(self, order):
        print("Замовлення збережено")


class OrderService:
    def __init__(
        self,
        calculator: PriceCalculator,
        invoice_generator: InvoiceGenerator,
        storage: OrderStorage
    ):
        self.calculator = calculator
        self.invoice_generator = invoice_generator
        self.storage = storage

    def process_order(self, order: Order):
        total = self.calculator.calculate(order)
        self.invoice_generator.generate(order, total)
        self.storage.save(order)
        return total


order = Order([100, 200, 300])

discount = PercentageDiscount(10)
calculator = PriceCalculator(discount)
invoice = InvoiceGenerator()
storage = FileOrderStorage()

service = OrderService(calculator, invoice, storage)

print("Підсумкова ціна:", service.process_order(order))


