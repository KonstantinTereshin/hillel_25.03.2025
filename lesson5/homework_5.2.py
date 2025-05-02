# ДЗ 5.2. Модифікувати калькулятор

print("Вітаю у калькуляторі!")

while True:

    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть дію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

    
    if operation == '+':
        result = num1 + num2
        print("Результат:", result)
    elif operation == '-':
        result = num1 - num2
        print("Результат:", result)
    elif operation == '*':
        result = num1 * num2
        print("Результат:", result)
    elif operation == '/':
        if num2 == 0:
            print("Помилка: ділення на нуль!")
            
        else:
            result = num1 / num2
            print("Результат:", result)
    else:
        print("Помилка: невідома операція!")
        

    
    continue_input = input("Бажаєте продовжити? (yes/y): ").lower() 


    if continue_input not in ['yes', 'y']:
        break

print("Роботу калькулятора завершено.")