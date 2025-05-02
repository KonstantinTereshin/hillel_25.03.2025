# x = range(20, 30, 2)
# for i in x:
#     print(i)

# import random
#
#
#
# print(random.random())
#
#
# print(random.randint(10, 100))
#
# lst = [1:4:2]
#

# tup = (1, 2, 3, 4)
# print(tup[0])



# ДЗ 4.1. Перемістити всі нулі до кінця списку

# def move_zeros_simple(lst):


#   non_zeros = [x for x in lst if x != 0]


#   zeros_count = lst.count(0)


#   zeros_list = [0] * zeros_count


#   return non_zeros + zeros_list


# list1 = [0, 1, 0, 12, 3]
# print(f"{list1} -> {move_zeros_simple(list1)}")

# list2 = [0]
# print(f"{list2} -> {move_zeros_simple(list2)}")

# list3 = [1, 0, 13, 0, 0, 0, 5]
# print(f"{list3} -> {move_zeros_simple(list3)}")

# list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# print(f"{list4} -> {move_zeros_simple(list4)}")



# ДЗ 4.2. Знайти суму елементів із парними індексами

# def calculate_sum_and_multiply(data):


#   if not data:
#     return 0
  

#   sum_even_indexed = sum(data[::2])
  

#   last_element = data[-1]
  

#   result = sum_even_indexed * last_element
  
#   return result


# print(calculate_sum_and_multiply([0, 1, 7, 2, 4, 8]))  
# print(calculate_sum_and_multiply([1, 3, 5]))         
# print(calculate_sum_and_multiply([6]))                
# print(calculate_sum_and_multiply([]))   



# ДЗ 4.3. Список із 3 елементів

import random


num_elements = random.randint(3, 10)


original_list = [random.randint(3, 10) for _ in range(num_elements)]

print(f"Початковий список: {original_list}")


new_list = [original_list[0], original_list[2], original_list[-2]]

print(f"Новий список: {new_list}")


print("Приклади:")
list1 = [1, 2, 3, 4, 5, 6, 7, 9]
print(f"{list1} == {[list1[0], list1[2], list1[-2]]}")

list2 = [1, 1, 2, 1]
print(f"{list2} == {[list2[0], list2[2], list2[-2]]}")

list3 = [6, 3, 7]
print(f"{list3} == {[list3[0], list3[2], list3[-2]]}")   