n = int(input('Введите количество чисел: '))

numbers = []

for _ in range(n):
    numbers.append(int(input()))

max_of_5 = max(num for num in numbers if num % 5 ==0)

print(max_of_5)


