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


# num1 = float(input("Введіть перше число: "))


# operation = input("Введіть дію (+, -, *, /): ")


# num2 = float(input("Введіть друге число: "))


# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':

#     if num2 == 0:
#         print("Помилка: ділення на нуль!")
#         exit()
#     else:
#         result = num1 / num2
# else:
#     print("Помилка: невідома операція!")
#     exit()


# print("Результат:", result)


#ДЗ 3.2. Перемістити елемент у списку

def move_last_to_first(input_list):
  

  if len(input_list) < 2:
    return input_list

  last_element = input_list[-1]


  remaining_elements = input_list[:-1]

  result_list = [last_element] + remaining_elements

  return result_list

list1 = [12, 3, 4, 10]
print(f"{list1} => {move_last_to_first(list1)}")

list2 = [1]
print(f"{list2} => {move_last_to_first(list2)}")

list3 = []
print(f"{list3} => {move_last_to_first(list3)}")

list4 = [12, 3, 4, 10, 8]
print(f"{list4} => {move_last_to_first(list4)}")
