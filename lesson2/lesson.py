# print("start!")
#
# x = int(input("Enter number: "))
#
# x *= 10
#
# # x ** 3
#
# print (x)
#
# x = input("Користувач ввів: ")
# y = x[::-1]
# print("На екрані відображається:", y)

#ДЗ 2.2. Необхідно "перевернути" 5-ти значне число

n = int(input("Користувач ввів: "))
rev = 0

rev = rev + (n % 10) * 10000
n = n // 10

rev = rev + (n % 10) * 1000
n = n // 10

rev = rev + (n % 10) * 100
n = n // 10

rev = rev + (n % 10) * 10
n = n // 10

rev = rev + (n % 10)

print("На екрані відображається:", rev)



#ДЗ 2.1. Виведення числа в стовпчик

n = int(input("Введіть 4-значне число: "))

d1 = (n // 1000) % 10
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

print(d1)
print(d2)
print(d3)
print(d4)
