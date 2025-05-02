#ДЗ 3.1. Найпростіший калькулятор


num1 = float(input("Введіть перше число: "))


operation = input("Введіть дію (+, -, *, /): ")


num2 = float(input("Введіть друге число: "))


if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':

    if num2 == 0:
        print("Помилка: ділення на нуль!")
        exit()
    else:
        result = num1 / num2
else:
    print("Помилка: невідома операція!")
    exit()


print("Результат:", result)