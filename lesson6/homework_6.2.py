#ДЗ 6.2. Конвертер із числа в дату

def format_seconds_to_time(total_seconds):

  seconds_in_day = 86400
  seconds_in_hour = 3600
  seconds_in_minute = 60


  days, remainder_after_days = divmod(total_seconds, seconds_in_day)
  hours, remainder_after_hours = divmod(remainder_after_days, seconds_in_hour)
  minutes, seconds = divmod(remainder_after_hours, seconds_in_minute)


  day_word = "днів"

  if days % 10 == 1 and days % 100 != 11:
      day_word = "день"

  elif days % 10 in [2, 3, 4] and days % 100 not in [12, 13, 14]:
      day_word = "дні"


  formatted_hours = str(hours).zfill(2)
  formatted_minutes = str(minutes).zfill(2)
  formatted_seconds = str(seconds).zfill(2)


  return f"{days} {day_word}, {formatted_hours}:{formatted_minutes}:{formatted_seconds}"


print(f"0 -> {format_seconds_to_time(0)}")
print(f"224930 -> {format_seconds_to_time(224930)}")
print(f"466289 -> {format_seconds_to_time(466289)}")
print(f"950400 -> {format_seconds_to_time(950400)}")
print(f"1209600 -> {format_seconds_to_time(1209600)}")
print(f"1900800 -> {format_seconds_to_time(1900800)}")
print(f"8639999 -> {format_seconds_to_time(8639999)}")
print(f"22493 -> {format_seconds_to_time(22493)}")
print(f"7948799 -> {format_seconds_to_time(7948799)}")