# x="test"

# x =x.encode("utf-8")
# print(type(x))
# print(x)

# x = x.decode("windows-1251")

# print(type(x))
# print(x)


# y = ["Vasya",21,2.1]

# x = {"name": "Vasya",
#      "age": 21,
#      "height": 2.1}

# print(y[0])
# print(x["name"])

# x["city"] = "Dnipro"

# print(x)
# print(x["city"])

# print("Vasya" in x)
# print("city" in x)

# print(hash("test"))  

#ДЗ 6.1. Діапазон букв

# import string

# def get_chars_between(char_range_str): 

#   char1, char2 = char_range_str.split('-')
#   all_letters = string.ascii_letters
#   index1 = all_letters.find(char1)
#   index2 = all_letters.find(char2)


#   return all_letters[index1:index2+1]


# print(get_chars_between("a-c"))
# print(get_chars_between("a-a"))
# print(get_chars_between("s-H"))
# print(get_chars_between("a-A"))

#ДЗ 6.2. Конвертер із числа в дату

# def format_seconds_to_time(total_seconds):

#   seconds_in_day = 86400
#   seconds_in_hour = 3600
#   seconds_in_minute = 60


#   days, remainder_after_days = divmod(total_seconds, seconds_in_day)
#   hours, remainder_after_hours = divmod(remainder_after_days, seconds_in_hour)
#   minutes, seconds = divmod(remainder_after_hours, seconds_in_minute)


#   day_word = "днів"

#   if days % 10 == 1 and days % 100 != 11:
#       day_word = "день"

#   elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
#       day_word = "дні"


#   formatted_hours = str(hours).zfill(2)
#   formatted_minutes = str(minutes).zfill(2)
#   formatted_seconds = str(seconds).zfill(2)


#   return f"{days} {day_word}, {formatted_hours}:{formatted_minutes}:{formatted_seconds}"


# print(f"0 -> {format_seconds_to_time(0)}")
# print(f"224930 -> {format_seconds_to_time(224930)}")
# print(f"466289 -> {format_seconds_to_time(466289)}")
# print(f"950400 -> {format_seconds_to_time(950400)}")
# print(f"1209600 -> {format_seconds_to_time(1209600)}")
# print(f"1900800 -> {format_seconds_to_time(1900800)}")
# print(f"8639999 -> {format_seconds_to_time(8639999)}")
# print(f"22493 -> {format_seconds_to_time(22493)}")
# print(f"7948799 -> {format_seconds_to_time(7948799)}")


#ДЗ 6.3. Добуток чисел
def multiply_digits_until_single(n):

  while n > 9:
    product = 1
    
    for digit_char in str(n):
      
      digit = int(digit_char)
      
      product *= digit
    
    n = product
  return n


user_input = input("Введіть ціле число: ")
number = int(user_input)

result = multiply_digits_until_single(number)
print(f"Результат: {result}")


# print(f"999 -> {multiply_digits_until_single(999)}")
# print(f"1000 -> {multiply_digits_until_single(1000)}")
# print(f"423 -> {multiply_digits_until_single(423)}")
# print(f"33 -> {multiply_digits_until_single(33)}")
# print(f"25 -> {multiply_digits_until_single(25)}")
# print(f"1 -> {multiply_digits_until_single(1)}")