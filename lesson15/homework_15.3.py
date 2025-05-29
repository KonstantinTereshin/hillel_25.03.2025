#ДЗ 15.3. Клас «Правильний дріб»
from fractions import Fraction

# Створюємо «правильні» дроби
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

# Додавання, віднімання, множення
f_c = f_b + f_a        # => Fraction(21, 18)
f_d = f_b * f_a        # => Fraction(6, 18)
f_e = f_a - f_b        # => Fraction(3, 18)

# Порівняння
print(f_d < f_c)       # True
print(f_d > f_e)       # True
print(f_a != f_b)      # True
print(Fraction(2, 4) == Fraction(3, 6))  # True

# Вивід
print(f_c)             # 21/18
print(f_d)             # 6/18
print(f_e)             # 3/18
