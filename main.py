from random import randint

# Заполнить массив случайными числами и выполнить
# циклический сдвиг элементов массива вправо на 1 элемент.


n = 5
a = [randint(1, 5) for i in range(n)]
print(*a)

last_el = a[-1]
for i in range(n-1, 0, -1):
    a[i] = a[i-1]
a[0] = last_el
print(*a)


# Cгенерируйте список из 40 случайных чисел от 20 до 40 и выведите его в строку.
# Найдите число, которое встречаетс чаще других в этом списке .
# Если их больше одного, выведите минимальное

numbers = [randint(20, 40) for i in range(n)]
n = 40
counts = {}
for num in numbers:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1
print(counts)
most_res_num = max(counts.values())
most_frequent_numbers = [num for num, count in counts.items() if count == most_res_num]
print(most_res_num)
if len(most_frequent_numbers) == 1:
    print("Число, которое встречается чаще других:", most_frequent_numbers[0])
else:
    print("Числа, которые встречаются чаще других:", min(most_frequent_numbers))

# Массив имеет четное число элементов.
# Заполнить массив случайными числами и выполнить реверс отдельно в первой половине и второй половине.

n = 6
a = [randint(1, 10) for i in range(n)]
print(*a)
a[:n//2] = a[n//2-1::-1]
a[n//2:] = a[n:n//2-1:-1]
print(*a)

# Заполнить массив случайными числами в интервале [-100,100] и переставить элементы так,
# чтобы все положительные элементы стояли в начала массива, а все отрицательные и нули - в конце.
# Вычислите количество положительных элементов.

n = 6
a = [randint(-100, 100)for i in range(n)]
print(*a)
k = 0
g = 0
while g < n - k:
    if a[g] <= 0:
        a.append(a.pop(g))
        k += 1
        g -= 1
    g += 1
print(n-k)
print(a)

# Заполнить массив случайными числами в интервале
# [-10,10] и отобрать в другой массив все чётные отрицательные числа.

n = 6
a = [randint(-10, 10)for i in range(n)]
u = []
print(*a)
for i in a:
    if i % 2 == 0 and i < 0:
        u.append(i)
print(*u)

