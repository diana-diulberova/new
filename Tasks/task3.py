# ✔Напишите функцию, которая открывает на чтение созданные в прошлых
# задачах файлы с числами и именами.
# ✔Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔если результат умножения отрицательный, сохраните имя записанное
# строчными буквами и произведение по модулю ✔если результат умножения положительный,
# сохраните имя прописными буквами и произведение округлённое до целого.
# ✔В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔При достижении конца более короткого файла, возвращайтесь в его начало.

def mult(names, numbers):
    result = 'results.txt'
    with(
        open(names, 'r', encoding='utf-8') as f_1,
        open(numbers, 'r', encoding='utf-8') as f_2,
        open(result, 'w', encoding='utf-8') as f_3
    ):
        res_mult = []
        for line in f_2:
            a, b = map(float, line.strip().split('|'))
            res_mult.append(a * b)
        res_name = []
        for line in f_1:
            res_name.append(line.strip())
        if len(res_mult) == max(len(res_name), len(res_mult)):
            for i in range(max(len(res_name), len(res_mult))):
                if i >= len(res_name):
                    j = i - len(res_name) - 1
                else:
                    j = i
                if res_mult[i] > 0:
                    res_mult[i] = int(res_mult[i])
                    res_name[j] = str(res_name[j]).upper()
                else:
                    res_mult[i] = abs(res_mult[i])
                    res_name[j] = str(res_name[j]).lower()
                f_3.write(f'{res_name[j]} {res_mult[i]}\n')
        else:
            for i in range(max(len(res_name), len(res_mult))):
                if i >= len(res_mult):
                    j = i - len(res_mult) - 1
                else:
                    j = i
                if res_mult[j] > 0:
                    res_mult[j] = int(res_mult[j])
                    res_name[i] = str(res_name[i]).upper()
                else:
                    res_mult[j] = abs(res_mult[j])
                    res_name[i] = str(res_name[i]).lower()
                f_3.write(f'{res_name[i]} {res_mult[j]}\n')


if __name__ == '__main__':
    names = r'C:\Users\Пользователь\Documents\IT\Geek Brains\HW_Python_GB\task_2.txt'
    numbers = r'C:\Users\Пользователь\Documents\IT\Geek Brains\HW_Python_GB\file_1.txt'
    mult(names, numbers)
