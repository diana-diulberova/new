# Напишите программу, которая принимает две строки вида “a/b” -
# дробь с числителем и знаменателем. Программа должна возвращать сумму и
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions

fraction_1 = input("Введите первую дробь (a/b): ")
fraction_2 = input("Введите вторую дробь (c/d): ")

a, b = map(int, fraction_1.split('/'))
c, d = map(int, fraction_2.split('/'))

common_denominator = b * d
sum_numerator = a * d + c * b
    
print(f"Сумма дробей: {sum_numerator}/{common_denominator}")

product_numerator = a * c
product_denominator = b * d
    
print(f"Произведение дробей: {product_numerator}/{product_denominator}")

first_fraction = fractions.Fraction(a, b)
second_fraction = fractions.Fraction(c, d)
result_1 = first_fraction + second_fraction
result_2 = first_fraction * second_fraction
print(result_1)
print(result_2)
