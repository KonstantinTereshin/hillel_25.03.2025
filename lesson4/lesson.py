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

def move_zeros_simple(lst):


  non_zeros = [x for x in lst if x != 0]


  zeros_count = lst.count(0)


  zeros_list = [0] * zeros_count


  return non_zeros + zeros_list


list1 = [0, 1, 0, 12, 3]
print(f"{list1} -> {move_zeros_simple(list1)}")

list2 = [0]
print(f"{list2} -> {move_zeros_simple(list2)}")

list3 = [1, 0, 13, 0, 0, 0, 5]
print(f"{list3} -> {move_zeros_simple(list3)}")

list4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
print(f"{list4} -> {move_zeros_simple(list4)}")

