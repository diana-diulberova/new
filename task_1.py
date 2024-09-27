# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 4, 2, 5, 3, 6, 1, 2, 7, 4, 5, 1, 9]

result_list = []

for element in my_list:
    if element not in result_list:
        result_list.append(element)

print(f'Список без дублирующих элементов: = {result_list}')
