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


print(f"999 -> {multiply_digits_until_single(999)}")
print(f"1000 -> {multiply_digits_until_single(1000)}")
print(f"423 -> {multiply_digits_until_single(423)}")
print(f"33 -> {multiply_digits_until_single(33)}")
print(f"25 -> {multiply_digits_until_single(25)}")
print(f"1 -> {multiply_digits_until_single(1)}")