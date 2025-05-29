#ДЗ 15.1. Клас «Прямокутник
from functools import total_ordering

@total_ordering
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        """Повертає площу прямокутника."""
        return self.width * self.height

    def __eq__(self, other):
        """Порівняння за площею на рівність."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __lt__(self, other):
        """Порівняння за площею на менше."""
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() < other.get_square()

    def __add__(self, other):
        """
        Складання двох прямокутників.
        Новий прямокутник матиме таку ж ширину, як у лівого операнда,
        а висоту обчислюємо так, щоб площа дорівнювала сумі площ.
        """
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        new_width = self.width
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __mul__(self, n):
        """
        Множення прямокутника на число n.
        Новий прямокутник матиме ту ж ширину, що й вихідний,
        а висоту таку, щоб площа збільшилась в n разів.
        """
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        new_width = self.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)

    __rmul__ = __mul__  # щоб працювало і n * rectangle

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


if __name__ == "__main__":
    r1 = Rectangle(2, 4)
    r2 = Rectangle(3, 6)

    # Тести
    assert r1.get_square() == 8, 'Test1'
    assert r2.get_square() == 18, 'Test2'

    r3 = r1 + r2
    assert r3.get_square() == 26, f'Test3: отримали {r3.get_square()}'

    r4 = r1 * 4
    assert r4.get_square() == 32, f'Test4: отримали {r4.get_square()}'

    assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

    # Додаткові перевірки порівнянь
    assert r1 < r2
    assert r4 > r2
    assert r1 <= Rectangle(1, 8)
    assert r2 >= Rectangle(9, 2)

    print("Усі тести пройдено успішно!")
    print(r3)  # Rectangle(width=2, height=13.0)
    print(r4)  # Rectangle(width=2, height=16.0)
