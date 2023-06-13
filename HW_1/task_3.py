# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

for i in range(1, 11):
   estimated_number = int(input("Угадайте число от 1 до 1000: "))
   if estimated_number == num:
      print("Поздравляю! Вы угадали число")
      break
   elif estimated_number > num:
      print("Не угадали! Число меньше", estimated_number)
   elif estimated_number < num:
      print("Не угадали! Число больше", estimated_number)
else:
   print("Вы исчерпали попытки угадать. Загаданное число равно", num)