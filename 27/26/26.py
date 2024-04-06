"""
На вход программы поступает последовательность
из N целых положительных чисел.
Рассматриваются все пары различных элементов последовательности.

Необходимо определить максимальную нечётную сумму пары.

Входные данные.

Даны два входных файла (файл A и файл B),
каждый из которых содержит в первой строке количество чисел
N (2 ≤ N ≤ 10000).
В каждой из последующих N строк записано одно целое положительное число,
не превышающее 100 000.

Программа должна вывести в первой строке одно число:
максимальную нечётную сумму пары.

Пример организации исходных данных во входном файле:
10
74
90
63
55
31
28
32
99
1
81

Для указанных входных данных значением искомой суммы
должно быть число 189.

В ответе укажите два числа:
сначала значение искомой суммы для файла А,
затем для файла B.

Предупреждение: для обработки файла B не следует использовать
переборный алгоритм, вычисляющий сумму для всех возможных вариантов,
поскольку написанная по такому алгоритму программа
будет выполняться слишком долго.
"""