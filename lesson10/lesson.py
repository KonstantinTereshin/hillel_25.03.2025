# def binari_search(itr, target):
#     low, high = 0, len(itr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if target == itr [mid]:
#             return mid
#         elif itr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

# def divide(a, b):
#     assert b != 0, "Делитель не может быть нулём!"
#     return a / b

# print(divide(10, 2))  # 5.0
# print(divide(10, 0))   # AssertionError: Делитель не может быть нулём!

file = open("text.txt", "r")  # Только чтение
content = file.read()
print(content)
file.close()

# with open(r"D:\hillel\hillel_25.03.2025\lesson10\text.txt", "a") as file:
#     content = file.write("123")
#     print(content)

# class Car:
#     count_of_wheels = 4

#     def __init__(self, brand: str, probig):
#         self.brand = brand
#         self.probig = probig

#     def stert(self):
#         print("Start engine")

# car = Car()    
# print(car.count_of_wheels)



#ДЗ 10.1. Генераторна функція

# def pow(x):
#     return x ** 2

# def some_gen(begin, end, func):
#     """
#     begin: перший елемент послідовності
#     end: кількість елементів у послідовності
#     func: функція, яка формує значення для послідовності
#     """
#     current = begin
#     for _ in range(end):
#         yield current
#         current = func(current)

# from inspect import isgenerator

# gen = some_gen(2, 4, pow)
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
# print('OK')



#ДЗ 10.2. Знайти перше слово

# import re

# def first_word(text):
#     """ Пошук першого слова """
#     # Використовуємо регулярний вираз для знаходження першого слова
#     match = re.search(r"[a-zA-Z']+", text)
#     return match.group(0) if match else ""

# assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word(".., and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
# print('OK')


#ДЗ 10.3. Перевірити чи є парним чи ні

# def is_even(digit):
#     """ Перевірка чи є парним число """
#     return digit % 2 == 0

# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')