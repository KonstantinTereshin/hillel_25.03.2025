# bool (0)
# bool([])

# print (5>2)
# print (5 == 5)
# print (5 != 5)
# # print (5 <> 5)

# if 5 > 2:
#     print("True")
# x =  5 > 2
# #
# if x:
#     print("True")

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


#ДЗ 3.2. Перемістити елемент у списку

def move_last_to_first(lst):

    if len(lst) < 2:
        return lst


    return [lst[-1]] + lst[:-1]



examples = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]

for example in examples:
    print(example, "=>", move_last_to_first(example))
