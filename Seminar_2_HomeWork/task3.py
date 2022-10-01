# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


import os
os.system('cls')

import math

def result_dictionary(n: int) -> list:
    new_list = [2]
    for num in range(1, n+1):
        new_list.append(num)
        new_list.append(math.ceil(new_list[-2]+(1+1/num)**num))
    new_list.pop(0)
    result_dict = {new_list[i] : new_list[i+1] for i in range(0, len(new_list), 2)}
    return result_dict

n = int(input('Введите натуральное число: '))
my_dictionary = result_dictionary(n)
print(result_dictionary(n))