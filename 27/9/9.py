"""
Дана последовательность N целых положительных чисел.

Необходимо определить количество пар элементов этой последовательности,
сумма элементов в которых равна числу 2000.
Порядок элементов в паре значения не имеет.

Входные данные:

Даны два входных файла (файл A и файл B),
каждый из которых содержит в первой строке натуральное число
N (3 ≤ N ≤ 10000) – количество чисел в последовательности.
В следующих N cтроках записаны числа, входящие в последовательность,
по одному в каждой строке.

Программа должна вывести одно число – количество найденных пар.

Пример входных данных:
6
400
100
1600
1200
100
800

Пример выходных данных для приведённого примера входных данных:
2

В ответе укажите два числа:
сначала значение искомой суммы для файла А,
затем для файла B.

Предупреждение: для обработки файла B не следует использовать
переборный алгоритм, вычисляющий сумму для всех возможных вариантов,
поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.
"""
