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