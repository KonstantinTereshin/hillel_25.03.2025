#ДЗ 12.2. Корзина для покупок
class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}  # ключ — екземпляр Item, значення — кількість

    def add_item(self, item, cnt):
        # замінюємо кількість, якщо товар уже є
        self.products[item] = cnt

    def get_total(self):
        # підсумовуємо вартість всіх товарів
        return sum(item.price * quantity for item, quantity in self.products.items())

    def __str__(self):
        lines = [f"User: {self.user}", "Items:"]
        for item, quantity in self.products.items():
            lines.append(f"{item.name}: {quantity} pcs.")
        return "\n".join(lines)


if __name__ == '__main__':
    # створюємо товари
    lemon = Item('lemon', 5, "yellow", "small")
    apple = Item('apple', 2, "red", "middle")
    print(lemon)   # lemon, price: 5

    # створюємо покупця
    buyer = User("Ivan", "Ivanov", "02628162")
    print(buyer)   # Ivan Ivanov

    # робимо замовлення
    cart = Purchase(buyer)
    cart.add_item(lemon, 4)
    cart.add_item(apple, 20)
    print(cart)
    """
    User: Ivan Ivanov
    Items:
    lemon: 4 pcs.
    apple: 20 pcs.
    """

    # перевіряємо загальну вартість
    assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
    assert cart.get_total() == 60, "Всього 60"

    # змінюємо кількість apple
    cart.add_item(apple, 10)
    print(cart)
    """
    User: Ivan Ivanov
    Items:
    lemon: 4 pcs.
    apple: 10 pcs.
    """

    assert cart.get_total() == 40, "Всього 40"
