# ДЗ 4.2. Знайти суму елементів із парними індексами

def calculate_sum_and_multiply(data):


  if not data:
    return 0
  

  sum_even_indexed = sum(data[::2])
  

  last_element = data[-1]
  

  result = sum_even_indexed * last_element
  
  return result


print(calculate_sum_and_multiply([0, 1, 7, 2, 4, 8]))  
print(calculate_sum_and_multiply([1, 3, 5]))         
print(calculate_sum_and_multiply([6]))                
print(calculate_sum_and_multiply([]))   