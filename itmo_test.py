# import math
#
# a = math.factorial(64)
# b = math.factorial(54)
# c = math.factorial(64 - 54)
#
# print(a / (b * c))

from math import comb, perm

# Данные задачи
n = 54  # общее количество символов
k = 6   # длина последовательности

# Число сочетаний (если порядок не важен)
combinations = comb(n, k)

# Число перестановок (если порядок важен)
permutations = perm(n, k)

print(combinations, permutations)
