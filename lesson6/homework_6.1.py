#ДЗ 6.1. Діапазон букв

import string

def get_chars_between(char_range_str): 

  char1, char2 = char_range_str.split('-')
  all_letters = string.ascii_letters
  index1 = all_letters.find(char1)
  index2 = all_letters.find(char2)


  return all_letters[index1:index2+1]


print(get_chars_between("a-c"))
print(get_chars_between("a-a"))
print(get_chars_between("s-H"))
print(get_chars_between("a-A"))