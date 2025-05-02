# ДЗ 3.3. Розділити один список на два списки

def split_list(input_list):

  n = len(input_list)

  
  if n == 0:
    return [[], []]
  else:
    split_point = (n + 1) // 2

    first_half = input_list[:split_point]
    second_half = input_list[split_point:]

    return [first_half, second_half]


print(f"[1, 2, 3, 4, 5, 6] => {split_list([1, 2, 3, 4, 5, 6])}")
print(f"[1, 2, 3] => {split_list([1, 2, 3])}")
print(f"[1, 2, 3, 4, 5] => {split_list([1, 2, 3, 4, 5])}")
print(f"[1] => {split_list([1])}")
print(f"[] => {split_list([])}")