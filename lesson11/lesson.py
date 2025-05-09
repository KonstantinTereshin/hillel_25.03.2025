
# #ДЗ 11.1. Генератор простих чисел
# def prime_generator(end):
#     for num in range(2, end + 1):
#         if num > 1:
#             is_prime = True
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 yield num

# from inspect import isgenerator

# gen = prime_generator(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
# assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
# assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
# print('Ok')


# #ДЗ 11.2. Заповнення списку кубами чисел
# def generate_cube_numbers(end):
#     num = 2
#     while True:
#         cube = num ** 3
#         if cube > end:
#             return
#         yield cube
#         num += 1

# from inspect import isgenerator

# gen = generate_cube_numbers(1)
# assert isgenerator(gen) == True, 'Test0'
# assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
# assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
# assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'

# #homework_11.3.py
# #ДЗ 11.3. Перевірка на парність.
# def is_even(number):
#     return (number & 1) == 0

# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'


# print('Hello', 'World')

# a = 4
# b = 5
# print(a + b)


# x = 'Welcome'
# print(x[3])

# x = "Hello World"
# print(
# len(x)
# )

# txt = "Hello World"
# x = txt[0]
# print(x)

# txt = 'The best things in life are free!'
# if 'free' in txt:
#   print('Yes, free is present in the text.')


# x = 'Welcome'
# print(x[3:5])

# txt = "Hello World"
# x = txt[2:5]
# print(x)

# x = 'Welcome'
# print(x[3:])

# x = 'Welcome'.upper()
# print(x)

# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# txt = " Hello World "
# x = txt.strip()
# print(x)


# txt = "Hello World"
# txt = txt.replace('H','J')
# print(txt)

# x = 'Welcome'
# y = 'Coders'
# print(x + y)

# print(bool("abc"))

# print(bool(0))

# x = 5 
# x += 3
# print(x)

# thislist = ['apple', 'banana', 'cherry']
# print(len(thislist))

# mylist = ['apple', 'banana', 'cherry']
# print(mylist[-1])

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[3:6])

# mylist = ['apple', 'banana', 'cherry']
# mylist[0] = 'kiwi'
# print(mylist[1])

# mylist = ['apple', 'banana', 'cherry']
# mylist.insert(0, 'orange')
# print(mylist[1])
# print(mylist)

# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits.insert(1,"lemon")
# print(fruits)


# mylist = ['apple', 'banana', 'cherry']
# i = 0
# while i < len(mylist):
#   print(mylist[i])
#   i = i + 1

# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits if x == 'banana']
# print(newlist)


# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits ]
# print(newlist)


# fruits = ['apple', 'banana', 'cherry']
# newlist = ['apple' for x in fruits]
# print(newlist)