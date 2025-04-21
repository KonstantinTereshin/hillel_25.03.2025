# x= "I lik'e Python"
# y= ('I like Python')
# z= """I like
# Python"""
#
# print(x)
# print(y)
# print(z)
#
# y= 100
# z = str(y)
# from lesson3.lesson import result

# x= "I lik'e Python"
#
# print(x[0])
# print(len(x))
# print(x[:6])
#
# for elem in x:
#     print(elem)

# x= "I like Python"
#
# print("like" in x)
#
# print("I like" + "Python")
#
# x= "I like Python"
# print(x.upper)

# name = input("Enter name: ")
# age = int(input("Enter age: "))

# print("Hello, %s, %d!" % (name,age))


# print(chr(65))

# ДЗ 5.1. Ім'я змінної

import string
import keyword

def is_valid_variable_name(name):

  
  if not name:
    return False

  
  if name in keyword.kwlist:
    return False


  if name.count('_') > 1:
      return False

 
  for i, char in enumerate(name):

    if char.isupper():
      return False


    if char.isspace():
      return False


    if char in string.punctuation and char != '_':
        return False


    if i == 0 and char.isdigit():
        return False


  return True

# print(f"_ => {is_valid_variable_name('_')}")
# print(f"__ => {is_valid_variable_name('__')}")
# print(f"___ => {is_valid_variable_name('___')}")
# print(f"x => {is_valid_variable_name('x')}")
# print(f"get_value => {is_valid_variable_name('get_value')}")
# print(f"get value => {is_valid_variable_name('get value')}")
# print(f"get!value => {is_valid_variable_name('get!value')}")
