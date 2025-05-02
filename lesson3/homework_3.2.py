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