"""
Дана последовательность N целых положительных чисел.

Необходимо определить количество пар элементов этой последовательности,
сумма которых делится на m = 80
и при этом хотя бы один элемент из пары больше b = 50000

Описание входных и выходных данных

Даны два входных файла (файл A и файл B),
каждый из которых содержит в первой строке входных данных
количество чисел N (2 ≤ N ≤ 10 000).
В каждой из последующих N строк записано одно натуральное число,
не превышающее 100 000.

Пример входных данных:
6
60
40
72040
30
40
120

Пример выходных данных для приведённого выше примера входных данных:3

В ответе укажите два числа:
сначала значение искомой суммы для файла А,
затем для файла B.

Предупреждение: для обработки файла B не следует использовать
переборный алгоритм, вычисляющий сумму для всех возможных вариантов,
поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.
"""