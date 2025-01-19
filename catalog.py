class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity})"
if __name__ == "__main__":
    product1 = Product("Laptop", 1500.00, 5)
    product2 = Product("Smartphone", 800.00, 10)
    print(product1)
    print(product2)

    print(f"Total value of {product1.name}: ${product1.total_value():.2f}")
    print(f"Total value of {product2.name}: ${product2.total_value():.2f}")
