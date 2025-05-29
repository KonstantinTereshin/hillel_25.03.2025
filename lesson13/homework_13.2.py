#ДЗ 13.2. Клас "Цифровий лічильник"
class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if start < self.min_value or start > self.max_value:
            raise ValueError(f"Початкове значення має бути в межах [{self.min_value}, {self.max_value}]")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError(f"Максимум не може бути меншим за мінімум ({self.min_value})")
        self.max_value = max_max
        # Якщо поточне значення вже вище нового максимуму — підкоригуємо його
        if self.current > self.max_value:
            self.current = self.max_value

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError(f"Мінімум не може бути більшим за максимум ({self.max_value})")
        self.min_value = min_min
        # Якщо поточне значення вже нижче нового мінімуму — підкоригуємо його
        if self.current < self.min_value:
            self.current = self.min_value

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Досягнуто максимум")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Досягнуто мінімум")

    def get_current(self):
        return self.current


if __name__ == "__main__":
    # Приклад тестів
    counter = Counter()
    counter.set_current(7)
    counter.step_up()
    counter.step_up()
    counter.step_up()
    assert counter.get_current() == 10, 'Test1'
    try:
        counter.step_up()  # має викинути ValueError
    except ValueError as e:
        print(e)  # Досягнуто максимум
    assert counter.get_current() == 10, 'Test2'

    counter.set_min(7)
    counter.step_down()
    counter.step_down()
    counter.step_down()
    assert counter.get_current() == 7, 'Test3'
    try:
        counter.step_down()  # має викинути ValueError
    except ValueError as e:
        print(e)  # Досягнуто мінімум
    assert counter.get_current() == 7, 'Test4'

    print("Усі тести пройшли успішно!")
